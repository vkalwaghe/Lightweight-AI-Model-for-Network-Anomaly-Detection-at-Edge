
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/
COPY models/ models/
COPY data/ data/

ENV PYTHONUNBUFFERED=1

CMD ["python", "src/inference_simulator.py", "--data", "data/sample_dataset_small.csv", "--model", "models/edge_model.tflite", "--scaler", "models/scaler_keras.pkl"]
