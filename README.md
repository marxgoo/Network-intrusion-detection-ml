# Network Intrusion Detection System 
**A Network Intrusion Detection System (NIDS)** is a security solution designed to monitor network traffic for suspicious or malicious activity. When it detects anything unusual such as known attack patterns, unauthorized access attempts, or policy violations—it generates alerts so administrators can take action.

# Data
The data used to train the classifier is taken from <a href="[https://example.com](https://www.kaggle.com/datasets/sampadab17/network-intrusion-detection)" target="_blank">Kaggle</a>. The dataset to be audited was provided which consists of a wide variety of intrusions simulated in a military network environment. It created an environment to acquire raw TCP/IP dump data for a network by simulating a typical US Air Force LAN.

# Features
The dataset comprises 41 features for each TCP/IP connection. These features are a mix of Categorical and Numerical data:

- **Categorical Features:** 3
- **Numerical Features:** 38
The features provide insights into the nature of the traffic, helping in distinguishing between normal and anomalous connections.

# Class Label

The class variable in the dataset categorizes the connections into two main categories:
- **Normal:** Connections that represent regular, non-malicious traffic.
- **Anomalous:** Connections that represent potential threats or attacks.
