# Your AI recommendation system shows users personalized offers. You measure how long it takes for users to click after seeing a recommendation.

# From historical data, you observe that the response time (in seconds) follows a logistic distribution:

# μ=5 (average 5 seconds)

# s=1.5 (scale, how spread out it is)

# You want to:

# Estimate the probability that a user clicks after 8 seconds or more — a delayed response.

import numpy as np
import matplotlib.pyplot as plt

# Logistic Distribution parameters
mu = 5        # mean response time (seconds)
s = 1.5       # scale (spread)
n_samples = 10000

# Simulate response times using logistic distribution
response_times = np.random.logistic(loc=mu, scale=s, size=n_samples)

# Calculate probability of response time >= 8 seconds
delayed_clicks = np.sum(response_times >= 8)
probability = delayed_clicks / n_samples

print(f"Estimated probability of delayed clicks (≥8s): {probability:.4f}")

# Plot histogram
plt.figure(figsize=(10,6))
plt.hist(response_times, bins=50, edgecolor='black', color='orange', density=True)
plt.axvline(8, color='red', linestyle='--', linewidth=2, label='8-second threshold')
plt.title("User Response Time (Logistic Distribution)", fontsize=14)
plt.xlabel("Response Time (seconds)")
plt.ylabel("Density")
plt.legend()
plt.grid(True)
plt.show()


