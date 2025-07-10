# “What is the probability that a GPS error exceeds 5 meters, assuming σ = 3?”

# We'll simulate 10,000 GPS errors from a Rayleigh distribution and compute the 
# probability that the error is greater than 5 meters.

import numpy as np
import matplotlib.pyplot as plt

# Rayleigh distribution parameters
sigma = 3         # scale parameter (standard deviation of x/y)
n_samples = 10000

# Simulate GPS position errors (distance from true location)
gps_errors = np.random.rayleigh(scale=sigma, size=n_samples)

# Probability error > 5 meters
threshold = 5
high_error = np.sum(gps_errors > threshold)
probability = high_error / n_samples

print(f"Estimated probability of GPS error > {threshold} meters: {probability:.4f}")

# Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(gps_errors, bins=50, color='dodgerblue', edgecolor='black', density=True)
plt.axvline(threshold, color='red', linestyle='--', linewidth=2, label=f'{threshold}m threshold')
plt.title("Rayleigh Distribution: GPS Position Error")
plt.xlabel("Position Error (meters)")
plt.ylabel("Density")
plt.legend()
plt.grid(True)
plt.show()
