# Intrusion Detection System (IDS) using CIC-IDS2017 & Machine Learning

## Overview

This repository presents a **real-time Intrusion Detection System (IDS)** built using machine learning models on the **CIC-IDS2017 dataset**, developed by the **Canadian Institute for Cybersecurity (CIC)**.

The project demonstrates:

- Dataset exploration and preprocessing
- Implementation and comparison of multiple machine learning models for **binary and multi-class classification**
- Deployment of the **best performing model (Random Forest)** for real-time network traffic analysis
- Alert generation for detected malicious traffic, similar to **Suricata alerts**

---

## Dataset Characteristics

- **Source:** CIC-IDS2017
- **Traffic Types:** Normal traffic and multiple attack types
- **Imbalance:** Majority of records labeled as `Benign`
- **Features:** 79 columns: 78 numerical features + 1 categorical `Label`
- **Network Flow Features:** Flow duration, packet lengths, ports, TCP/UDP flags, bytes per second, packets per second, etc.

---

## Project Contents

### Exploratory Data Analysis (EDA)
- Understand data distribution, correlations, and imbalance

### Data Preprocessing
- Feature selection, scaling, encoding, and handling missing values

### Machine Learning Models
Implemented models:

- Logistic Regression
- Support Vector Machine (SVM)
- Random Forest Classifier
- Naive Bayes
- K-Nearest Neighbors (KNN)

### Performance Evaluation
- Metrics: Accuracy, Precision, Recall, F1-score, Confusion Matrix
- Discussion on the impact of class imbalance

---

## Best Model Deployment

The **Random Forest Classifier** was trained with the following selected features:

```python
selected_features = [
    'Protocol',
    'Flow Duration',
    'Tot Fwd Pkts',
    'Tot Bwd Pkts',
    'TotLen Fwd Pkts',
    'TotLen Bwd Pkts',
    'Fwd Pkt Len Mean',
    'Bwd Pkt Len Mean',
    'Flow Byts/s',
    'Flow Pkts/s',
    'Pkt Len Mean',
    'Pkt Len Std',
    'SYN Flag Cnt',
    'ACK Flag Cnt',
    'FIN Flag Cnt',
    'RST Flag Cnt',
    'PSH Flag Cnt',
    'URG Flag Cnt'
]
