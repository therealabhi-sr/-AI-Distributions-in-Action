# AI/ML Distributions in Action: Real-World Simulated Use Cases 📊🤖

This repository presents **real-world applications of core probability distributions** through **high-fidelity simulations** in Python. These simulations reflect how AI/ML systems use probability distributions for tasks like anomaly detection, behavior modeling, system optimization, and more.

Each script demonstrates:
- A real-world problem statement
- An appropriate distribution-based modeling approach
- Python code using NumPy/Matplotlib for simulation
- Probability estimation and visualization
- Practical implications for AI/ML systems

---

## 📦 Distributions Covered

| Distribution | Use Case |
|--------------|----------|
| **Normal** | Face Recognition System – Reaction time delay |
| **Binomial** | Spam Classifier – Minimum accuracy detection |
| **Poisson** | AI Security System – Rare motion event detection |
| **Uniform** | Maintenance Scheduling – Late-night random checks |
| **Logistic** | Recommender System – User click delay modeling |
| **Exponential** | Smart Elevator System – Wait time estimation |
| **Chi-Square** | Vending Machine – Coin fraud detection |
| **Rayleigh** | GPS System – Positioning error analysis |
| **Pareto** | Revenue Modeling – High-value customer distribution |

---

## 📁 File Overview

Each file is a standalone Python script:

- `1_Normal_distribution.py`: Estimate the chance a face detection system takes longer than 400 ms to respond.
- `2_Binomial_Distribution.py`: Calculate how likely a spam filter correctly classifies at least 18 out of 20 emails.
- `3_Poisson_Distribution.py`: Determine the rarity of 12+ motion detections in a night with an AI security system.
- `4_uniform_distribution.py`: Model when random maintenance occurs between 2–4 AM and the odds of it starting after 3:30.
- `5_Logistic_distribution.py`: Simulate delayed user clicks (≥8s) in a recommender system.
- `7_exponential_distribution.py`: Compute how often elevator wait times exceed 5 minutes.
- `8_Chi_square_Distribution.py`: Run a chi-square test to detect suspicious coin usage in a vending machine.
- `9_Rayleigh_Distribution.py`: Estimate GPS error probabilities exceeding 5 meters.
- `10_Pareto_Distribution.py`: Identify high-revenue users generating more than ₹5 using Pareto modeling.

---

## 🔧 Setup Instructions

### Prerequisites
- Python ≥ 3.7
- Libraries: `numpy`, `matplotlib`, `scipy` (for exponential example)

### Install Requirements
```bash
pip install numpy matplotlib scipy
