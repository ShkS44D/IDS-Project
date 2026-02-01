# Sentinel AI | Network Intrusion Detection System (IDS)

**Sentinel AI** is a high-performance, machine-learning-driven security command center designed to monitor network traffic and identify anomalies in real time. By leveraging a **Random Forest** classification model, the system achieves near-perfect accuracy in distinguishing between normal traffic and potential network breaches.

## Key Features

* **AI-Powered Detection:** Utilizes a trained Random Forest model with **99.8% precision** to identify network threats.
* **Real-Time Dashboard:** A professional "Command Center" interface built with **Streamlit** for monitoring system load, active sensors, and mitigated threats.
* **Live Threat Analysis:** simulate or verify incoming packets against the AI engine to receive instant "Normal" or "Anomaly" classifications with confidence scores.
* **Deep Analytics:** Visualizes feature importance (e.g., `src_bytes`, `dst_bytes`) using **Plotly** to explain the AI's decision-making process.

## Tech Stack

* **Language:** Python.
* **Frameworks:** Streamlit (UI), Scikit-learn (ML), Pandas (Data Handling).
* **Visualization:** Plotly Express.
* **Security Focus:** Network Traffic Analysis & Anomaly Detection.

## Project Structure

To run this project, ensure your directory is organized as follows to match the asset-loading logic:

```text
├── app.py                # Main Streamlit application
├── models/               # Directory for ML artifacts
│   ├── RandomForest_model.pkl
│   ├── scaler.pkl
│   ├── label_encoders.pkl
│   ├── feature_names.pkl
│   └── validation_with_labels.csv
└── requirements.txt

```

## Getting Started

### 1. Prerequisites

* Python 3.8+
* Virtual environment (recommended)

### 2. Installation

```bash
git clone https://github.com/yourusername/Sentinel-AI.git
cd Sentinel-AI
pip install -r requirements.txt

```

### 3. Execution

Run the command center using Streamlit:

```bash
streamlit run app.py

```

## Model Performance

The system primarily analyzes network indicators like source and destination bytes relative to duration. A sudden spike in these values is a strong indicator of DDoS or port-scan patterns, which the model flags with high confidence.

## Author

**Muhammad Saad Ahmed**

**LinkedIn:** [shsaadahmed](https://www.linkedin.com/in/shsaadahmed/) 

 **Focus:** Cybersecurity Student | Penetration Tester
