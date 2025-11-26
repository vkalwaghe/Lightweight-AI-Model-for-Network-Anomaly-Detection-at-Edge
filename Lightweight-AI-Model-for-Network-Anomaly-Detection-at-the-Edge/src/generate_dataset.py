# src/generate_dataset.py
import numpy as np
import pandas as pd
from tqdm import tqdm
import argparse
import os

np.random.seed(42)

def sample_benign():
    packet_rate = np.random.normal(50, 10)
    avg_pkt_size = np.random.normal(600, 100)
    std_pkt_size = np.random.normal(100, 30)
    dst_port_count = np.random.poisson(3)
    tcp_flag_ratio = np.random.uniform(0.1, 0.5)
    inter_arrival_mean = np.random.normal(0.02, 0.01)
    return [packet_rate, avg_pkt_size, std_pkt_size, dst_port_count, tcp_flag_ratio, inter_arrival_mean]

def sample_ddos():
    packet_rate = np.random.normal(2000, 300)
    avg_pkt_size = np.random.normal(200, 50)
    std_pkt_size = np.random.normal(50, 10)
    dst_port_count = np.random.poisson(1)
    tcp_flag_ratio = np.random.uniform(0.05, 0.2)
    inter_arrival_mean = np.random.normal(0.0005, 0.0002)
    return [packet_rate, avg_pkt_size, std_pkt_size, dst_port_count, tcp_flag_ratio, inter_arrival_mean]

def sample_spoofing():
    packet_rate = np.random.normal(300, 80)
    avg_pkt_size = np.random.normal(500, 120)
    std_pkt_size = np.random.normal(120, 40)
    dst_port_count = np.random.poisson(5)
    tcp_flag_ratio = np.random.uniform(0.4, 0.9)
    inter_arrival_mean = np.random.normal(0.01, 0.008)
    return [packet_rate, avg_pkt_size, std_pkt_size, dst_port_count, tcp_flag_ratio, inter_arrival_mean]

def sample_portscan():
    packet_rate = np.random.normal(150, 40)
    avg_pkt_size = np.random.normal(120, 30)
    std_pkt_size = np.random.normal(30, 10)
    dst_port_count = np.random.poisson(30)
    tcp_flag_ratio = np.random.uniform(0.05, 0.3)
    inter_arrival_mean = np.random.normal(0.005, 0.003)
    return [packet_rate, avg_pkt_size, std_pkt_size, dst_port_count, tcp_flag_ratio, inter_arrival_mean]

def make_dataset(n_per_class=2000, out="data/dataset.csv"):
    rows = []
    for _ in tqdm(range(n_per_class), desc="benign"):
        rows.append(sample_benign() + [0])
    for _ in tqdm(range(n_per_class), desc="ddos"):
        rows.append(sample_ddos() + [1])
    for _ in tqdm(range(n_per_class), desc="spoofing"):
        rows.append(sample_spoofing() + [2])
    for _ in tqdm(range(n_per_class), desc="portscan"):
        rows.append(sample_portscan() + [3])

    df = pd.DataFrame(rows, columns=[
        "packet_rate","avg_pkt_size","std_pkt_size","dst_port_count",
        "tcp_flag_ratio","inter_arrival_mean","label"
    ])
    df[["packet_rate","avg_pkt_size","std_pkt_size","dst_port_count",
        "tcp_flag_ratio","inter_arrival_mean"]] = \
        df[["packet_rate","avg_pkt_size","std_pkt_size","dst_port_count",
            "tcp_flag_ratio","inter_arrival_mean"]].clip(lower=0.0001)
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    df.to_csv(out, index=False)
    print("Saved", out)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=2000)
    parser.add_argument("--out", type=str, default="data/dataset.csv")
    args = parser.parse_args()
    make_dataset(n_per_class=args.n, out=args.out)
