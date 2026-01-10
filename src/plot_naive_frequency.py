import pandas as pd
import matplotlib.pyplot as plt

from load_data import load_allele_frequencies

def plot_naive_frequency():
    """
    Naive visualization of allele frequency by population.
    This plot is intentionally simplistic and easy to misinterpret.
    """
    df = load_allele_frequencies()

    # Focus on a single variant (rs4244285, CYP2C19)
    variant_df = df[df["variant"] == "rs4244285"]

    variant_df = variant_df.sort_values("allele_frequency", ascending=False)

    plt.figure(figsize=(10, 6))
    plt.barh(
        variant_df["genetic_ancestry_group"],
        variant_df["allele_frequency"]
    )
    plt.xlabel("Allele Frequency")
    plt.title("Allele Frequency of CYP2C19 Variant by Population")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_naive_frequency()

