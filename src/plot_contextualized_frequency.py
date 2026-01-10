import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Load data
df = pd.read_csv("data/allele_frequencies.csv", comment="#")

# Hardy–Weinberg genotype frequencies
p = df["allele_frequency"]
df["homozygous_reference"] = (1 - p) ** 2
df["heterozygous"] = 2 * p * (1 - p)
df["homozygous_variant"] = p ** 2

# Sort for readability
df = df.sort_values("allele_frequency", ascending=True)

# Output directory
os.makedirs("figures", exist_ok=True)

# Plot
plt.figure(figsize=(9, 4))

y = np.arange(len(df))

plt.barh(
    y,
    df["homozygous_reference"],
    label="No *2 allele",
    color="#c7e9c0"
)
plt.barh(
    y,
    df["heterozygous"],
    left=df["homozygous_reference"],
    label="One *2 allele",
    color="#74c476"
)
plt.barh(
    y,
    df["homozygous_variant"],
    left=df["homozygous_reference"] + df["heterozygous"],
    label="Two *2 alleles",
    color="#238b45"
)

plt.yticks(y, df["genetic_ancestry_group"])
plt.xlabel("Expected proportion of individuals")
plt.title("CYP2C19*2: Population Allele Frequency vs Expected Genotypes")

plt.legend(loc="lower right")
plt.tight_layout()
plt.savefig("figures/contextualized_genotype_distribution.png", dpi=150)
plt.close()

print("Saved genotype distribution plot to figures/contextualized_genotype_distribution.png")

