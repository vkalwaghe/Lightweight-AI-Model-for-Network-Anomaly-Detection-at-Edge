# Lightweight AI Model for Network Anomaly Detection (Prototype)

This is a prototype that demonstrates a lightweight ML pipeline for edge-based network anomaly detection:
- synthetic dataset generation
- training a tiny Keras model and exporting to TFLite
- TFLite inference simulator (measures latency)
- live capture inference (requires `scapy` and root)

## Setup (Linux / macOS)
```bash
# 1. create venv
python3 -m venv venv
source venv/bin/activate

# 2. install deps
pip install -r requirements.txt

@'
# Lightweight AI Model for Network Anomaly Detection at the Edge

Prototype demonstrating:
- micro-flow feature extraction from packet windows
- lightweight ML model (Keras MLP) + TFLite export
- RF baseline and benchmarking for edge deployment
- small demo scripts for simulation and live capture

## Quick start (local)
1. create and activate venv:
   python -m venv venv
   venv\Scripts\activate

2. install deps:
   pip install -r requirements.txt

3. generate dataset:
   python src/generate_dataset.py --n 800 --out data/dataset.csv

4. train (baseline + Keras):
   python src/train_cv.py --data data/dataset.csv --out models --epochs 6

5. export to TFLite:
   python src/export_tflite.py --keras models/keras_full.h5 --scaler models/scaler_keras.pkl --out models/edge_model.tflite

6. run simulator:
   python src/inference_simulator.py --data data/dataset.csv --model models/edge_model.tflite --scaler models/scaler_keras.pkl
'@ > README.md
