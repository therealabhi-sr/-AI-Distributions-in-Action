# AI-Based Face Recognition: Reaction Time Analyzer

# You’re building a face recognition system and measure the reaction time (in milliseconds) it takes to detect a face.

# The system's reaction times follow a Normal Distribution:

# Mean (μ) = 300 ms

# Standard deviation (σ) = 50 ms

# You want to know:

# What’s the probability that the system takes more than 400 ms to respond?

# This is a tail probability problem for a Normal distribution.

import numpy as np
import matplotlib.pyplot as plt

# Parameters
μ = 300   # average reaction time in ms
σ = 50    # standard deviation
n_simulations = 10000

# Simulate 10,000 reaction times
reaction_times = np.random.normal(μ, σ, n_simulations)

# Count how many times reaction > 400ms
slow_responses = np.sum(reaction_times > 400)

# Estimate probability
probability = slow_responses / n_simulations

print(f"Estimated probability of >400 ms response: {probability:.4f}")

# Plot
plt.hist(reaction_times, bins=50, color='skyblue', edgecolor='black')
plt.axvline(400, color='red', linestyle='--', label='400 ms threshold')
plt.title("Normal Distribution of Face Recognition Response Time")
plt.xlabel("Reaction Time (ms)")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)
plt.show()
