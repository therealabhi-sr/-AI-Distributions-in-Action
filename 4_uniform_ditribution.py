# The AI camera performs maintenance randomly between 2:00 AM and 4:00 AM every night.
# Simulate 10,000 nights and estimate the probability that the maintenance starts after 3:30 AM.

import numpy as np
import matplotlib.pyplot as plt

# Define uniform range in hours (2 AM to 4 AM → 2 to 4)
a = 2.0
b = 4.0
n_simulations = 10000

# Generate random maintenance times
maintenance_times = np.random.uniform(a, b, n_simulations)

# Count how many times it happens after 3:30 AM (3.5 in hours)
late_maintenance = np.sum(maintenance_times >= 3.5)

# Estimate probability
probability = late_maintenance / n_simulations

print(f"Estimated probability of maintenance after 3:30 AM: {probability:.4f}")

# Plot
plt.hist(maintenance_times, bins=30, edgecolor='black', color='lightgreen')
plt.axvline(3.5, color='red', linestyle='--', label='3:30 AM threshold')
plt.title("Uniform Distribution of Maintenance Times (2 AM - 4 AM)")
plt.xlabel("Time of Maintenance (Hours)")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)
plt.show()

