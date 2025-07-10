# You're developing an AI-based smart elevator system in a high-rise building. Elevators arrive randomly, but on average, one arrives every 3 minutes.

# You want to model and optimize:

# How long a person is expected to wait before the next elevator arrives.

# This is a classic case for the Exponential Distribution because:

# The elevator arrivals are random and independent.

# You only care about how long until the next event.

# The system is memoryless: waiting for 2 minutes doesn’t reduce how much longer you’ll wait.

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

# Elevator system parameters
mean_wait = 3  # average time between elevators (minutes)
lambda_rate = 1 / mean_wait  # λ = 1/mean
threshold = 5  # waiting threshold (minutes)

# Simulate 10,000 elevator wait times
n_samples = 10000
wait_times = np.random.exponential(scale=mean_wait, size=n_samples)

# Calculate empirical probability of wait ≥ threshold
long_waits = np.sum(wait_times >= threshold)
probability = long_waits / n_samples

print(f"Estimated P(wait ≥ {threshold} minutes): {probability:.4f}")

# Plot histogram
plt.figure(figsize=(10,6))
plt.hist(wait_times, bins=50, color='mediumseagreen', edgecolor='black', density=True)
plt.axvline(threshold, color='red', linestyle='--', linewidth=2, label=f'{threshold}-minute threshold')
plt.title("Elevator Wait Times (Exponential Distribution)", fontsize=14)
plt.xlabel("Wait Time (minutes)")
plt.ylabel("Density")
plt.legend()
plt.grid(True)
plt.show()
