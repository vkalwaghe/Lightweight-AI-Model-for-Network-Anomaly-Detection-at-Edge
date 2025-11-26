# src/pcap_to_csv.py
"""
Simple PCAP -> CSV microflow extractor.
Requires: pyshark (or edit to use tshark CLI)
Generates one window per fixed time interval (e.g., 1 second).
"""
import pyshark
import argparse
import csv
import os
from collections import defaultdict
from src.features import window_features_from_packets

class SimplePkt:
    def __init__(self, time, length, has_tcp, has_udp, dport):
        self.time = time
        self.length = length
        self.has_tcp = has_tcp
        self.has_udp = has_udp
        self.dport = dport

def extract_windows_from_pcap(pcap_path, window_size=1.0):
    cap = pyshark.FileCapture(pcap_path, keep_packets=False)
    windows = defaultdict(list)
    start_time = None
    for pkt in cap:
        try:
            ts = float(pkt.sniff_timestamp)
            if start_time is None:
                start_time = ts
            window_idx = int((ts - start_time) // window_size)
            length = int(pkt.length) if hasattr(pkt, 'length') else (int(pkt.captured_length) if hasattr(pkt,'captured_length') else 0)
            has_tcp = hasattr(pkt, 'tcp')
            has_udp = hasattr(pkt, 'udp')
            dport = None
            if has_tcp:
                try: dport = int(pkt.tcp.dstport)
                except: dport = None
            elif has_udp:
                try: dport = int(pkt.udp.dstport)
                except: dport = None
            spkt = SimplePkt(time=ts, length=length, has_tcp=has_tcp, has_udp=has_udp, dport=dport)
            windows[window_idx].append(spkt)
        except Exception:
            continue
    cap.close()
    # convert windows to rows
    rows = []
    for idx in sorted(windows.keys()):
        features = window_features_from_packets(windows[idx])
        rows.append(features.tolist())
    return rows

def write_csv(rows, out_csv):
    os.makedirs(os.path.dirname(out_csv) or ".", exist_ok=True)
    header = ["packet_rate","avg_pkt_size","std_pkt_size","dst_port_count","tcp_flag_ratio","inter_arrival_mean"]
    with open(out_csv, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        for r in rows:
            w.writerow(r)
    print("Wrote CSV:", out_csv)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pcap", required=True)
    parser.add_argument("--out", default="data/pcap_features.csv")
    parser.add_argument("--window", type=float, default=1.0)
    args = parser.parse_args()
    rows = extract_windows_from_pcap(args.pcap, window_size=args.window)
    write_csv(rows, args.out)
