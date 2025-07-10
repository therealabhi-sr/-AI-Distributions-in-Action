# You run a vending machine that accepts coins. Over time, you’ve collected data on
# what coin types (₹1, ₹2, ₹5) users insert, and you know their expected usage pattern from past data:

# ₹1 → 40%

# ₹2 → 35%

# ₹5 → 25%

# Now, in one particular week, you notice a suspicious pattern:

# ₹1 → 30 coins

# ₹2 → 50 coins

# ₹5 → 20 coins

# You want to know:

# Is this unusual enough to suspect someone is inserting fake coins?

# This is where the Chi-Square Goodness-of-Fit Test comes in — to measure whether the
# observed frequencies differ significantly from the expected frequencies.

import numpy as np
import matplotlib.pyplot as plt

# Observed coin usage
observed = np.array([30, 50, 20])

# Historical expected ratio
expected_ratio = np.array([0.40, 0.35, 0.25])
total = np.sum(observed)
expected = expected_ratio * total

# Compute Chi-Square statistic manually
chi_square_stat = np.sum((observed - expected) ** 2 / expected)

# Degrees of Freedom = number of categories - 1
df = len(observed) - 1

# Critical value for df=2 at 99% confidence
critical_value_99 = 9.210

# Decision
if chi_square_stat > critical_value_99:
    decision = "❌ Suspicious usage detected (Significant deviation)"
else:
    decision = "✅ Usage is normal (No significant deviation)"

# Print results
print(f"Chi-Square Statistic: {chi_square_stat:.4f}")
print(f"Critical Value (99% confidence, df=2): {critical_value_99}")
print(f"Decision: {decision}")

# Visualization
coin_labels = ['₹1', '₹2', '₹5']
x = np.arange(len(coin_labels))
bar_width = 0.35

plt.figure(figsize=(10, 6))
plt.bar(x - bar_width/2, observed, width=bar_width, color='orange', edgecolor='black', label='Observed')
plt.bar(x + bar_width/2, expected, width=bar_width, color='seagreen', edgecolor='black', label='Expected')
plt.xticks(x, coin_labels)
plt.xlabel("Coin Type")
plt.ylabel("Frequency")
plt.title("Chi-Square Test: Observed vs Expected Coin Usage")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
