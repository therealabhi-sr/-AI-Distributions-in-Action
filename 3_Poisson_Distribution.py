# Your AI-based security system sees on average 5 motion events per night (λ = 5).
# One night, you observe 12 events.
# Use NumPy to simulate 10,000 nights and estimate the probability of 12 or more events occurring
import numpy as np
import matplotlib.pyplot as plt

# Parameters
λ = 5                   # average events per night
observed = 12           # observed events
n_simulations = 10000   # simulate 10,000 nights

# Generate synthetic data from Poisson distribution
simulated_events = np.random.poisson(λ, n_simulations)

# Count how many nights had 12 or more events
anomalies = np.sum(simulated_events >= observed)

# Estimate probability
probability = anomalies / n_simulations

print(f"Estimated probability of 12 or more events: {probability:.5f}")

# Decision
if probability < 0.01:
    print("⚠️ Anomaly Detected! (rare event)")
else:
    print("✅ Normal fluctuation.")

plt.hist(simulated_events, bins=range(0, 20), edgecolor='black', color='skyblue')
plt.axvline(observed, color='red', linestyle='--', label='Observed = 12')
plt.title("Poisson Simulation of Motion Events (λ=5)")
plt.xlabel("Motion Events Per Night")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)
plt.show()

# Out of 10,000 simulated nights, only 63 nights had 12 or more motion events.
# This implies that if your AI security system operates every night for ~27 years (10,000 nights),
# you would expect only 63 nights to be that active.