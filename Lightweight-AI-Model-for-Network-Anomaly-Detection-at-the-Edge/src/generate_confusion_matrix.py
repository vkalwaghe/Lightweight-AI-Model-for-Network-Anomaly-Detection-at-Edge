
---

## 3) `src/generate_confusion_matrix.py` (creates `docs/confusion_matrix.png`)
Create `src/generate_confusion_matrix.py` and paste (this will produce `docs/confusion_matrix.png`):

```python
# src/generate_confusion_matrix.py
"""
Generate a confusion matrix PNG from a CSV containing y_true and y_pred.
Usage:
    python src/generate_confusion_matrix.py --preds path/to/predictions.csv --out docs/confusion_matrix.png

predictions.csv should have two columns: label,true_pred
example:
label,y_pred
0,0
1,1
...
"""
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report

def make_plot(y_true, y_pred, labels, outpath):
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=[str(l) for l in labels])
    fig, ax = plt.subplots(figsize=(6,6))
    disp.plot(include_values=True, cmap='Blues', ax=ax, colorbar=False)
    ax.set_title("Confusion Matrix")
    plt.tight_layout()
    os.makedirs(os.path.dirname(outpath) or ".", exist_ok=True)
    plt.savefig(outpath, dpi=150)
    print("Saved confusion matrix to", outpath)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--preds", default="data/sample_predictions.csv", help="CSV with columns: label,y_pred")
    parser.add_argument("--out", default="docs/confusion_matrix.png")
    args = parser.parse_args()

    df = pd.read_csv(args.preds)
    if 'label' not in df.columns or 'y_pred' not in df.columns:
        raise SystemExit("CSV must contain columns: label,y_pred")

    labels = sorted(df['label'].unique())
    make_plot(df['label'].values, df['y_pred'].values, labels, args.out)
    print("\nClassification report:\n")
    from sklearn.metrics import classification_report
    print(classification_report(df['label'].values, df['y_pred'].values, zero_division=0))
