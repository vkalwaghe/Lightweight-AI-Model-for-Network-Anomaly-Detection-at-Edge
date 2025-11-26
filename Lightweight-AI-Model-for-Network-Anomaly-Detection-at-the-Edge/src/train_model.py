# src/train_model.py
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow import keras
import argparse
import os
from sklearn.metrics import classification_report, confusion_matrix
import joblib

def load_data(path="data/dataset.csv"):
    df = pd.read_csv(path)
    X = df.drop(columns=["label"]).values.astype(np.float32)
    y = df["label"].values.astype(np.int32)
    return X, y

def build_model(input_dim, n_classes):
    model = keras.Sequential([
        keras.layers.Input(shape=(input_dim,)),
        keras.layers.Dense(64, activation="relu"),
        keras.layers.Dense(32, activation="relu"),
        keras.layers.Dense(n_classes, activation="softmax")
    ])
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    return model

def convert_to_tflite(keras_model, X_sample, out_path="models/edge_model.tflite"):
    converter = tf.lite.TFLiteConverter.from_keras_model(keras_model)
    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    def rep_gen():
        for i in range(min(100, X_sample.shape[0])):
            x = X_sample[i:i+1]
            yield [x]
    try:
        converter.representative_dataset = rep_gen
        tflite_model = converter.convert()
    except Exception as e:
        print("Quantization conversion failed; converting float model instead:", e)
        converter.representative_dataset = None
        tflite_model = converter.convert()
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "wb") as f:
        f.write(tflite_model)
    print("Wrote TFLite model to", out_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="data/dataset.csv")
    parser.add_argument("--outdir", default="models")
    parser.add_argument("--epochs", type=int, default=20)
    args = parser.parse_args()

    X, y = load_data(args.data)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    scaler = StandardScaler().fit(X_train)
    X_train_s = scaler.transform(X_train)
    X_test_s = scaler.transform(X_test)

    model = build_model(input_dim=X.shape[1], n_classes=len(np.unique(y)))
    model.summary()
    model.fit(X_train_s, y_train, validation_split=0.1, epochs=args.epochs, batch_size=64, verbose=2)

    preds = np.argmax(model.predict(X_test_s), axis=1)
    print("Classification report:")
    print(classification_report(y_test, preds))
    print("Confusion matrix:")
    print(confusion_matrix(y_test, preds))

    os.makedirs(args.outdir, exist_ok=True)
    keras_path = os.path.join(args.outdir, "edge_model.h5")
    model.save(keras_path)
    print("Saved Keras model to", keras_path)

    joblib.dump(scaler, os.path.join(args.outdir, "scaler.pkl"))
    print("Saved scaler to", os.path.join(args.outdir, "scaler.pkl"))

    convert_to_tflite(model, X_train_s, out_path=os.path.join(args.outdir, "edge_model.tflite"))
