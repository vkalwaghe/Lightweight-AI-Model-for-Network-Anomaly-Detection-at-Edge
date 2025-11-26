# src/train_cv.py
import argparse
import os
import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
import tensorflow as tf
from tensorflow import keras

def build_keras(input_dim, n_classes):
    model = keras.Sequential([
        keras.layers.Input(shape=(input_dim,)),
        keras.layers.Dense(64, activation='relu'),
        keras.layers.Dense(32, activation='relu'),
        keras.layers.Dense(n_classes, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

def train_and_evaluate(csv_path="data/dataset.csv", outdir="models", n_splits=5, epochs=15):
    df = pd.read_csv(csv_path)
    X = df.drop(columns=['label']).values.astype(np.float32)
    y = df['label'].values.astype(int)
    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)

    best_rf = None
    best_score = 0.0

    # small RF baseline
    for train_idx, test_idx in skf.split(X, y):
        Xtr, Xte = X[train_idx], X[test_idx]
        ytr, yte = y[train_idx], y[test_idx]
        scaler = StandardScaler().fit(Xtr)
        Xtr_s = scaler.transform(Xtr)
        Xte_s = scaler.transform(Xte)
        rf = RandomForestClassifier(n_estimators=50, max_depth=10, random_state=42, n_jobs=-1)
        rf.fit(Xtr_s, ytr)
        score = rf.score(Xte_s, yte)
        if score > best_score:
            best_score = score
            best_rf = (rf, scaler)
    print("Best RF cross-val score:", best_score)
    os.makedirs(outdir, exist_ok=True)
    joblib.dump(best_rf[0], os.path.join(outdir, "rf_baseline.pkl"))
    joblib.dump(best_rf[1], os.path.join(outdir, "scaler_rf.pkl"))

    # Train Keras model on full train/test split
    from sklearn.model_selection import train_test_split
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    scaler = StandardScaler().fit(Xtr)
    Xtr_s = scaler.transform(Xtr)
    Xte_s = scaler.transform(Xte)
    model = build_keras(input_dim=X.shape[1], n_classes=len(np.unique(y)))
    model.fit(Xtr_s, ytr, validation_split=0.1, epochs=epochs, batch_size=64, verbose=2)
    preds = np.argmax(model.predict(Xte_s), axis=1)
    print("Keras classification report:")
    print(classification_report(yte, preds))
    model.save(os.path.join(outdir, "keras_full.h5"))
    joblib.dump(scaler, os.path.join(outdir, "scaler_keras.pkl"))
    print("Saved models to", outdir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="data/dataset.csv")
    parser.add_argument("--out", default="models")
    parser.add_argument("--epochs", type=int, default=20)
    args = parser.parse_args()
    train_and_evaluate(csv_path=args.data, outdir=args.out, epochs=args.epochs)
