# “What’s the probability that a user generates more than 5x the average revenue, 
# if revenue follows a Pareto distribution with shape α = 2.5 and min = ₹1?”

# We simulate user revenue and calculate how many exceed ₹5.

import numpy as np
import matplotlib.pyplot as plt

# Pareto distribution parameters
alpha = 2.5  # shape parameter
xm = 1       # minimum revenue in ₹
n_samples = 10000

# Generate Pareto-distributed user revenues
revenues = (np.random.pareto(alpha, n_samples) + 1) * xm

# Calculate P(revenue > 5)
threshold = 5
high_spenders = np.sum(revenues > threshold)
probability = high_spenders / n_samples

print(f"Estimated probability of revenue > ₹{threshold}: {probability:.4f}")

# Plot
plt.figure(figsize=(10, 6))
plt.hist(revenues, bins=100, density=True, color='orchid', edgecolor='black')
plt.axvline(threshold, color='red', linestyle='--', label=f'₹{threshold} threshold')
plt.title("Pareto Distribution: User Revenue Contribution")
plt.xlabel("Revenue (₹)")
plt.ylabel("Density")
plt.legend()
plt.grid(True)
plt.xlim(1, 20)  # zoom in for better view
plt.tight_layout()
plt.show()
