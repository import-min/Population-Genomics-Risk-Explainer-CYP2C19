import pandas as pd
import matplotlib.pyplot as plt
import os

# Load data
df = pd.read_csv("data/allele_frequencies.csv", comment="#")

# Sanity check
assert "allele_frequency" in df.columns
assert len(df) > 0

# Sort for nicer visualization
df = df.sort_values("allele_frequency", ascending=True)

# Create output directory
os.makedirs("figures", exist_ok=True)

# Plot
plt.figure(figsize=(8, 4))
plt.barh(
    df["genetic_ancestry_group"],
    df["allele_frequency"]
)

plt.xlabel("Allele Frequency")
plt.title("Naive View: CYP2C19*2 Frequency by Population")

plt.tight_layout()
plt.savefig("figures/naive_allele_frequency.png", dpi=150)
plt.close()

print("Saved naive plot to figures/naive_allele_frequency.png")

