# Latency benchmarking — inference & end-to-end

This file explains how to measure inference latency and end-to-end (capture→features→inference→action) latency for the prototype, and shows example results.

## Benchmark goals
- **Model inference latency**: time to run model inference on one feature vector.
- **End-to-end latency**: packet capture (1s window) → feature extraction → inference → optional action.
- **Throughput**: how many windows/sec the pipeline can handle.
- **Resource usage**: CPU% and memory at runtime.

## How to measure (local laptop)
1. Ensure model and scaler exist:
