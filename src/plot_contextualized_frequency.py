import pandas as pd
import matplotlib.pyplot as plt

from load_data import load_allele_frequencies

def plot_contextualized_frequency():
    """
    Context-aware visualization of allele frequency.
    Emphasizes population distribution rather than individual risk.
    """
    df = load_allele_frequencies()

    variant_df = df[df["variant"] == "rs4244285"]
    variant_df = variant_df.sort_values("allele_frequency", ascending=True)

    plt.figure(figsize=(10, 6))
    plt.barh(
        variant_df["genetic_ancestry_group"],
        variant_df["allele_frequency"],
        color="gray"
    )

    plt.xlabel("Allele Frequency (Population-Level)")
    plt.title(
        "Population Distribution of a CYP2C19 Variant\n"
        "Allele frequency does NOT equal individual risk"
    )

    plt.figtext(
        0.5,
        -0.15,
        "This plot shows how common a variant is across populations.\n"
        "Clinical relevance depends on gene function, environment, dosage, and dominance — not frequency alone.",
        wrap=True,
        horizontalalignment="center",
        fontsize=9
    )

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_contextualized_frequency()

