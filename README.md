# 🛡️ EdgeSentinel — Lightweight AI for Network Anomaly Detection

<p align="center">
  <b>Edge AI • Network Security • Machine Learning • Anomaly Detection • Lightweight Inference</b>
</p>

<p align="center">
  A resource-efficient AI framework for detecting abnormal network behavior at the edge with low-latency and lightweight machine learning inference.
</p>

---

## 📌 Project Overview

**EdgeSentinel** is a lightweight Artificial Intelligence system developed by **Vaibhav Kalwaghe** for detecting anomalous network activity directly at the edge.

Traditional network security systems often send large volumes of network traffic or telemetry to centralized servers for analysis. This can introduce additional latency, bandwidth requirements, and dependency on cloud infrastructure.

This project explores an **Edge AI approach**, where a lightweight machine learning model can analyze network-related data closer to the source and identify potentially abnormal behavior.

The project focuses on:

* Network anomaly detection
* Lightweight machine learning
* Edge AI
* Low-latency inference
* Resource-efficient model deployment
* Network security analytics
* Automated anomaly classification

---

# 🎯 Objectives

The main objectives of EdgeSentinel are:

* Detect abnormal network behavior using machine learning
* Develop a lightweight model suitable for edge environments
* Reduce dependency on centralized processing
* Enable faster anomaly detection
* Create a modular ML pipeline
* Provide a foundation for real-time network monitoring
* Evaluate model performance using standard classification metrics

---

# 🧠 Why Edge-Based Anomaly Detection?

In a traditional architecture:

```text
Network Traffic
      │
      ▼
Central Server / Cloud
      │
      ▼
ML Model
      │
      ▼
Anomaly Detection
```

This approach can introduce:

* Network latency
* Additional bandwidth usage
* Cloud dependency
* Centralized processing overhead

An edge-oriented architecture moves the analysis closer to the data source:

```text
Network Traffic
      │
      ▼
┌──────────────────┐
│   Edge Device    │
│                  │
│ Lightweight ML   │
│      Model       │
└────────┬─────────┘
         │
         ▼
   Anomaly Detection
         │
    ┌────┴────┐
    ▼         ▼
 Normal    Anomaly
```

This architecture is particularly useful for environments where quick detection and efficient resource utilization are important.

---

# 🏗️ System Architecture

```text
                       NETWORK ENVIRONMENT
                              │
                              ▼
                     Network Data / Features
                              │
                              ▼
                    ┌───────────────────┐
                    │ Data Preprocessing│
                    │                   │
                    │ Cleaning          │
                    │ Transformation    │
                    │ Feature Handling  │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Lightweight ML    │
                    │ Model             │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Anomaly Detection │
                    └─────────┬─────────┘
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
                 Normal              Anomaly
                    │                   │
                    └─────────┬─────────┘
                              ▼
                         Alert / Log
```

---

# 🔄 Machine Learning Pipeline

The complete machine learning workflow is:

```text
Raw Network Data
       │
       ▼
Data Preparation
       │
       ▼
Feature Processing
       │
       ▼
Model Training
       │
       ▼
Model Evaluation
       │
       ▼
Model Optimization
       │
       ▼
Edge Deployment
       │
       ▼
Real-Time Inference
       │
       ▼
Anomaly Detection
```

---

# 🧩 Project Structure

```text
Lightweight-AI-Model-for-Network-Anomaly-Detection-at-the-Edge/
│
├── deploy/
│   └── Deployment configuration
│
├── docs/
│   └── Project documentation
│
├── src/
│   └── Source code
│
├── tests/
│   └── Test cases
│
├── README.md
│
└── requirements.txt
```

The project follows a modular structure separating source code, deployment resources, documentation, and testing.

---

# 🛠️ Technology Stack

| Technology           | Purpose                                |
| -------------------- | -------------------------------------- |
| **Python**           | Core development and ML implementation |
| **Machine Learning** | Network anomaly detection              |
| **NumPy**            | Numerical processing                   |
| **Pandas**           | Data processing                        |
| **Scikit-learn**     | Model training and evaluation          |
| **Matplotlib**       | Data visualization                     |
| **Pytest**           | Automated testing                      |
| **Git/GitHub**       | Version control                        |

> The exact libraries used depend on the implementation and are defined in `requirements.txt`.

---

# 🔍 Network Anomaly Detection

The system treats network behavior as a collection of measurable features.

Conceptually:

```text
Network Event
      │
      ├── Traffic Features
      ├── Connection Features
      ├── Packet Features
      ├── Protocol Information
      └── Statistical Features
              │
              ▼
       Machine Learning Model
              │
              ▼
       ┌──────┴──────┐
       ▼             ▼
    Normal        Anomalous
```

The model learns patterns in network data and identifies observations that differ significantly from expected behavior.

---

# 🤖 Lightweight AI Approach

A major focus of the project is **resource-efficient inference**.

Edge environments may have constraints such as:

* Limited CPU
* Limited memory
* Limited storage
* Limited power
* Restricted network connectivity

Therefore, an edge-oriented model should balance:

```text
Detection Accuracy
       +
Inference Speed
       +
Memory Efficiency
       +
Computational Cost
```

The objective is not simply to build the largest possible model, but to develop a model that is practical for constrained environments.

---

# 📊 Model Evaluation

The trained model can be evaluated using standard classification metrics.

### Accuracy

Measures the overall percentage of correctly classified samples.

```text
Accuracy =
Correct Predictions
───────────────────
Total Predictions
```

### Precision

Measures how many predicted anomalies are actually anomalous.

```text
Precision =
True Positives
────────────────────────
True Positives + False Positives
```

### Recall

Measures how many actual anomalies were successfully detected.

```text
Recall =
True Positives
────────────────────────
True Positives + False Negatives
```

### F1 Score

Balances precision and recall.

```text
F1 =
2 × Precision × Recall
──────────────────────
Precision + Recall
```

For security applications, **recall is particularly important** because failing to detect a genuine anomaly can have significant consequences.

---

# ⚡ Edge Inference

The deployment workflow is designed around local inference:

```text
Network Data
     │
     ▼
Edge Device
     │
     ▼
Preprocessing
     │
     ▼
Lightweight Model
     │
     ▼
Prediction
     │
 ┌───┴────┐
 ▼        ▼
Normal   Anomaly
```

This approach can reduce the need to continuously transfer raw network information to a centralized server.

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/vkalwaghe/Lightweight-AI-Model-for-Network-Anomaly-Detection-at-Edge.git
```

Navigate to the project directory:

```bash
cd Lightweight-AI-Model-for-Network-Anomaly-Detection-at-Edge
```

Create a virtual environment:

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

After installing the dependencies, the project components can be executed according to the implementation provided in the `src/` and `deploy/` directories.

General workflow:

```text
Prepare Data
     ↓
Preprocess Data
     ↓
Train Model
     ↓
Evaluate Model
     ↓
Deploy Model
     ↓
Run Edge Inference
     ↓
Detect Anomalies
```

---

# 🧪 Testing

The project includes a `tests/` directory for validating important components.

Run the test suite using:

```bash
pytest
```

Testing helps verify:

* Data processing
* Model functionality
* Prediction logic
* Utility functions
* Deployment-related components

---

# 📁 Source Code Organization

The project separates development responsibilities into different directories.

### `src/`

Contains the core implementation of the anomaly detection system.

### `deploy/`

Contains deployment-related resources for running the model in an edge-oriented environment.

### `docs/`

Contains supporting documentation and technical information.

### `tests/`

Contains automated tests for project components.

---

# 🔐 Security Applications

Network anomaly detection can be used as a defensive security mechanism for identifying potentially suspicious behavior.

Potential applications include:

* Intrusion detection
* Network monitoring
* IoT security
* Edge device security
* Industrial network monitoring
* Smart infrastructure
* Enterprise network security
* Cybersecurity monitoring

---

# 🌐 Edge AI Use Cases

The architecture can be adapted for environments such as:

### IoT Networks

```text
IoT Devices
     ↓
Edge Gateway
     ↓
AI Anomaly Detection
     ↓
Security Alert
```

### Industrial Systems

```text
Sensors / Machines
       ↓
Edge Computing Node
       ↓
ML Detection
       ↓
Abnormal Activity Alert
```

### Smart Infrastructure

```text
Network Devices
       ↓
Edge Processing
       ↓
Anomaly Detection
       ↓
Central Monitoring
```

---

# 💡 Key Concepts Demonstrated

This project demonstrates practical knowledge of:

### Artificial Intelligence

* Machine learning
* Classification
* Anomaly detection
* Model evaluation
* Feature processing

### Cybersecurity

* Network security
* Intrusion detection concepts
* Security monitoring
* Abnormal behavior detection

### Edge Computing

* Edge AI
* Local inference
* Resource-efficient models
* Low-latency processing

### Software Engineering

* Modular project structure
* Testing
* Deployment organization
* Version control

---

# 🏆 Project Highlights

### 🛡️ Security-Focused AI

Combines machine learning with network security to identify abnormal network behavior.

### ⚡ Edge-Oriented

Designed with resource efficiency and local inference in mind.

### 🤖 Lightweight Model

Focuses on practical ML deployment rather than computationally expensive architectures.

### 📊 Measurable Evaluation

Uses standard machine-learning metrics to evaluate detection performance.

### 🧩 Modular Design

Separates source code, deployment resources, documentation, and tests.

### 🔬 Research Potential

Provides a foundation for future research in Edge AI, network security, and intelligent intrusion detection.

---

# 🔮 Future Enhancements

Potential improvements include:

* [ ] Real-time packet analysis
* [ ] Streaming network telemetry
* [ ] Online learning
* [ ] Adaptive anomaly thresholds
* [ ] Model quantization
* [ ] Model pruning
* [ ] Knowledge distillation
* [ ] ONNX-based deployment
* [ ] TensorFlow Lite / edge runtime support
* [ ] Docker-based deployment
* [ ] IoT gateway integration
* [ ] Real-time security dashboard
* [ ] Alert notification system
* [ ] Federated learning
* [ ] Explainable AI for anomaly predictions
* [ ] Edge-to-cloud monitoring architecture

---

# 🔬 Research Direction

The project can be extended toward research in:

```text
                 Edge AI Security
                        │
        ┌───────────────┼───────────────┐
        │               │               │
        ▼               ▼               ▼
   Lightweight      Federated       Explainable
       AI            Learning            AI
        │               │               │
        └───────────────┼───────────────┘
                        ▼
               Intelligent Security
```

Future research can investigate how model compression, distributed learning, and edge computing can improve network anomaly detection while maintaining detection performance.

---

# 📈 Possible Advanced Architecture

A future version can combine edge and cloud processing:

```text
                  NETWORK
                     │
                     ▼
               Edge Gateway
                     │
              Lightweight AI
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
       Normal                Anomaly
          │                     │
          │                     ▼
          │              Local Security
          │                  Alert
          │
          ▼
       Cloud / SIEM
          │
          ▼
     Long-Term Analytics
```

This hybrid architecture can combine the speed of edge inference with the analytical capabilities of centralized infrastructure.

---

# 👨‍💻 Author

## Vaibhav Kalwaghe

**Information Technology Undergraduate**

### Technical Interests

```text
Artificial Intelligence
Machine Learning
Cybersecurity
Edge Computing
Data Engineering
Cloud Computing
Adversarial Machine Learning
Secure AI Systems
```

---

# ⭐ Conclusion

**EdgeSentinel** demonstrates how lightweight machine learning can be applied to network anomaly detection in resource-constrained edge environments.

The project combines **AI, cybersecurity, and edge computing** to create a foundation for faster and more efficient network security monitoring.

The system can be further developed toward real-time network monitoring, model optimization, IoT security, federated learning, and intelligent edge-based intrusion detection.
