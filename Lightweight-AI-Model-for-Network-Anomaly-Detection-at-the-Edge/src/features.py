# src/features.py
import numpy as np

FEATURE_NAMES = [
    "packet_rate", "avg_pkt_size", "std_pkt_size",
    "dst_port_count", "tcp_flag_ratio", "inter_arrival_mean"
]

def window_features_from_packets(pkts):
    """
    pkts: iterable of packet-like objects with attributes:
          - time (float)
          - length (int)
          - has_tcp (bool)
          - has_udp (bool)
          - dport (int or None)
    Return: numpy array of features (len=6)
    """
    if len(pkts) == 0:
        return np.zeros(len(FEATURE_NAMES), dtype=np.float32)

    times = np.array([p.time for p in pkts], dtype=float)
    lengths = np.array([p.length for p in pkts], dtype=float)

    packet_rate = len(pkts) / max(1.0, (times.max() - times.min())) if len(pkts) > 1 else len(pkts)
    avg_pkt_size = float(lengths.mean())
    std_pkt_size = float(lengths.std())
    dst_ports = set([p.dport for p in pkts if getattr(p, "dport", None) is not None])
    dst_port_count = len(dst_ports)
    tcp_flags = sum([1 for p in pkts if getattr(p, "has_tcp", False)])
    tcp_flag_ratio = tcp_flags / max(1, len(pkts))
    inter_arrival = np.diff(np.sort(times)) if len(times) > 1 else np.array([0.0])
    inter_arrival_mean = float(inter_arrival.mean())

    return np.array([packet_rate, avg_pkt_size, std_pkt_size, dst_port_count, tcp_flag_ratio, inter_arrival_mean], dtype=np.float32)
