# You’re building a lightweight LLM for mobile devices in healthcare.
# After processing 1 million unique tokens, you want to know:

# 🔹 How much token usage will be covered by the top 10,000 tokens?
# 🔹 Does this justify limiting your vocabulary to just 10,000 tokens to reduce model size?

import numpy as np
import matplotlib.pyplot as plt

# Zipf parameters
s = 1.2               # Zipf exponent (realistic for NLP)
total_tokens = 1_000_000  # Total unique tokens in dataset
top_k = 10_000        # Vocabulary size limit

# Step 1: Compute Zipf weights (unnormalized frequencies)
ranks = np.arange(1, total_tokens + 1)
zipf_weights = 1 / ranks**s

# Step 2: Compute coverage by top_k tokens
top_weight = np.sum(zipf_weights[:top_k])
total_weight = np.sum(zipf_weights)
coverage = top_weight / total_weight

print(f"Top {top_k} tokens cover approximately {coverage * 100:.2f}% of token usage.")

# Step 3: Plot cumulative coverage curve
cumulative_coverage = np.cumsum(zipf_weights[:top_k]) / total_weight

plt.figure(figsize=(10, 6))
plt.plot(np.arange(1, top_k + 1), cumulative_coverage, color='crimson', linewidth=2)
plt.axhline(coverage, color='blue', linestyle='--', label=f"Top {top_k} coverage: {coverage*100:.2f}%")
plt.title("Cumulative Coverage of Token Usage (Zipf Distribution)", fontsize=14)
plt.xlabel("Token Rank")
plt.ylabel("Cumulative Token Usage (%)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
