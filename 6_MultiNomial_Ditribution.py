# From historical data, you observe that the probability of a user reading an article from 
# each category in a session (of 10 articles) is:

# Politics → 0.3

# Business → 0.2

# Sports → 0.4

# Technology → 0.1

# You want to simulate a large number of such reading sessions and estimate the probability
# that in a session of 10 articles, the user reads exactly:

# 3 Politics

# 2 Business

# 4 Sports

# 1 Technology

# Let’s solve this using the Multinomial Distribution.

import numpy as np 
import matplotlib.pyplot as plt

import numpy as np
from scipy.stats import multinomial
import matplotlib.pyplot as plt

# Define the number of trials (articles read per session)
n_articles = 10

# Category probabilities
probabilities = [0.3, 0.2, 0.4, 0.1]  # [Politics, Business, Sports, Tech]

# Target outcome: [3 Politics, 2 Business, 4 Sports, 1 Tech]
observed_counts = [3, 2, 4, 1]

# Calculate exact probability of this outcome
prob = multinomial.pmf(observed_counts, n_articles, probabilities)
print(f"Probability of reading pattern [3,2,4,1]: {prob:.4f}")

# Simulate 10000 user sessions
n_simulations = 10000
samples = np.random.multinomial(n_articles, probabilities, size=n_simulations)

# Count how many times the target pattern occurred
match = np.sum(np.all(samples == observed_counts, axis=1))
empirical_prob = match / n_simulations

print(f"Empirical probability from simulation: {empirical_prob:.4f}")

# Plot histogram for Sports articles read per session
sports_counts = samples[:, 2]
plt.figure(figsize=(10,6))
plt.hist(sports_counts, bins=np.arange(0, 12)-0.5, edgecolor='black', color='skyblue', density=True)
plt.axvline(4, color='red', linestyle='--', label="Target: 4 Sports articles")
plt.title("Distribution of 'Sports' Articles Read per Session", fontsize=14)
plt.xlabel("Number of Sports Articles")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)
plt.show()
