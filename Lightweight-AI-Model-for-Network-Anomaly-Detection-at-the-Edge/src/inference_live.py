# src/inference_live.py
from scapy.all import sniff
import numpy as np
import joblib
import argparse
from tensorflow.lite.python.interpreter import Interpreter

def extract_features_from_window(pkts):
    if len(pkts)==0:
        return np.zeros(6, dtype=np.float32)
    packet_rate = len(pkts)
    sizes = [len(p) for p in pkts]
    avg_pkt_size = np.mean(sizes)
    std_pkt_size = np.std(sizes)
    dst_ports = set()
    tcp_flag_count = 0
    inter_times = []
    last_ts = None
    for p in pkts:
        try:
            if p.haslayer("TCP") or p.haslayer("UDP"):
                if hasattr(p.payload, 'dport'):
                    dst_ports.add(int(p.payload.dport))
            if p.haslayer("TCP"):
                tcp_flag_count += 1
        except Exception:
            pass
        if last_ts is None:
            last_ts = p.time
        else:
            inter_times.append(p.time - last_ts)
            last_ts = p.time
    dst_port_count = len(dst_ports)
    tcp_flag_ratio = tcp_flag_count / max(1, len(pkts))
    inter_arrival_mean = np.mean(inter_times) if inter_times else 0.0
    return np.array([packet_rate, avg_pkt_size, std_pkt_size, dst_port_count, tcp_flag_ratio, inter_arrival_mean], dtype=np.float32)

def load_interpreter(path):
    interp = Interpreter(model_path=path)
    interp.allocate_tensors()
    return interp

def tflite_predict(interp, x):
    input_details = interp.get_input_details()
    output_details = interp.get_output_details()
    x = x.astype(input_details[0]['dtype'])
    x = np.reshape(x, input_details[0]['shape'])
    interp.set_tensor(input_details[0]['index'], x)
    interp.invoke()
    out = interp.get_tensor(output_details[0]['index'])
    return out

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="models/edge_model.tflite")
    parser.add_argument("--scaler", default="models/scaler.pkl")
    parser.add_argument("--iface", default=None)
    parser.add_argument("--window", type=float, default=1.0)
    args = parser.parse_args()

    scaler = joblib.load(args.scaler)
    interp = load_interpreter(args.model)

    labels = {0:"benign",1:"ddos",2:"spoofing",3:"portscan"}
    print("Starting live sniffing. Press Ctrl+C to stop.")
    while True:
        pkts = sniff(timeout=args.window, iface=args.iface)
        feats = extract_features_from_window(pkts)
        feats_s = scaler.transform(feats.reshape(1,-1))
        out = tflite_predict(interp, feats_s)
        pred = int(np.argmax(out))
        print(f"Window detected: {labels.get(pred,'?')} (scores: {out.flatten()})")
