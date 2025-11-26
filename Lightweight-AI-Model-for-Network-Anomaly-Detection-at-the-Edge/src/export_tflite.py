# src/export_tflite.py
import argparse
import joblib
import numpy as np
import tensorflow as tf
from tensorflow import keras
import os

def representative_gen(X_sample):
    for i in range(min(100, X_sample.shape[0])):
        yield [X_sample[i:i+1].astype(np.float32)]

def convert(keras_path, scaler_path, out_path="models/keras_quant.tflite"):
    model = keras.models.load_model(keras_path)
    scaler = joblib.load(scaler_path)
    # build representative data from scaler: try to load sample data from same dir (assume data/dataset.csv exists)
    import pandas as pd
    df = pd.read_csv("data/dataset.csv")
    X = df.drop(columns=["label"]).values.astype(np.float32)
    Xs = scaler.transform(X)
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    converter.representative_dataset = lambda: representative_gen(Xs)
    try:
        tflite_model = converter.convert()
    except Exception as e:
        print("Quantization error:", e)
        tflite_model = converter.convert()
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "wb") as f:
        f.write(tflite_model)
    print("Saved tflite to", out_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--keras", default="models/keras_full.h5")
    parser.add_argument("--scaler", default="models/scaler_keras.pkl")
    parser.add_argument("--out", default="models/edge_model.tflite")
    args = parser.parse_args()
    convert(args.keras, args.scaler, out_path=args.out)
