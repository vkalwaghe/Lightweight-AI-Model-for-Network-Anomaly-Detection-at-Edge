# src/inference_simulator.py
import numpy as np
import pandas as pd
import time
import joblib
import argparse
from tensorflow.lite.python.interpreter import Interpreter

def load_interpreter(tflite_path):
    interp = Interpreter(model_path=tflite_path)
    interp.allocate_tensors()
    return interp

def predict_tflite(interpreter, x):
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    x = x.astype(input_details[0]['dtype'])
    x = np.reshape(x, input_details[0]['shape'])
    interpreter.set_tensor(input_details[0]['index'], x)
    start = time.time()
    interpreter.invoke()
    t = (time.time() - start) * 1000.0
    out = interpreter.get_tensor(output_details[0]['index'])
    return out, t

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="data/dataset.csv")
    parser.add_argument("--model", default="models/edge_model.tflite")
    parser.add_argument("--scaler", default="models/scaler.pkl")
    args = parser.parse_args()

    df = pd.read_csv(args.data)
    X = df.drop(columns=["label"]).values.astype(np.float32)
    y = df["label"].values.astype(int)

    scaler = joblib.load(args.scaler)
    Xs = scaler.transform(X)

    interp = load_interpreter(args.model)

    latencies = []
    correct = 0
    n = 0
    for i in range(0, len(Xs)):
        x = Xs[i:i+1]
        out, t = predict_tflite(interp, x)
        latencies.append(t)
        pred = int(np.argmax(out))
        if pred == y[i]:
            correct += 1
        n += 1
        if i % 200 == 0:
            print(f"Processed {i}/{len(Xs)} - latest latency {t:.2f} ms")
    print("Accuracy:", correct / n)
    print("Latency mean (ms):", np.mean(latencies), "p50:", np.percentile(latencies,50))
