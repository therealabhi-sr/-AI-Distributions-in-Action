# Spam Classifier: Email Detection Accuracy

# You’ve trained a spam classifier.

# The model has a 90% accuracy on individual emails.

# You test it on a batch of 20 emails.

# You want to know:

# What’s the probability that the classifier correctly detects at least 18 emails?
# (i.e., 18, 19, or 20 correct classifications)

# This is a Binomial Distribution problem:

# n = 20 (trials)

# p = 0.9 (success probability)

# We want: 
# P(X ≥ 18) = P(X = 18) + P(X = 19) + P(X = 20)
# where X is the number of correct classifications.
# P(X≥18)

import numpy as np
import matplotlib.pyplot as plt

# Parameters
n = 20         # number of emails
p = 0.9        # probability of correct classification
trials = 10000 # number of simulations

# Simulate binomial outcomes
correct_counts = np.random.binomial(n, p, trials)

# Calculate probability
successes = np.sum(correct_counts >= 18)
probability = successes / trials
print(f"Probability of ≥18 correct classifications: {probability:.4f}")

# Plotting
plt.figure(figsize=(10,6))
plt.hist(correct_counts, bins=np.arange(n+2)-0.5, edgecolor='black', color='lightcoral', rwidth=0.9)
plt.axvline(18, color='blue', linestyle='--', linewidth=2, label='Threshold: 18 correct')
plt.title("Spam Classification Accuracy (Binomial Distribution)", fontsize=14)
plt.xlabel("Correct Predictions (out of 20)")
plt.ylabel("Frequency")
plt.xticks(range(0, n+1))
plt.legend()
plt.grid(True)
plt.show()

