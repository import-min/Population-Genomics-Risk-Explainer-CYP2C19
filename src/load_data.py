import pandas as pd

DATA_PATH = "data/allele_frequencies.csv"

def load_allele_frequencies(path=DATA_PATH):
    """
    Load allele frequency data derived from gnomAD.
    Returns a pandas DataFrame with basic validation.
    """
    df = pd.read_csv(path, comment="#")

    required_cols = {
        "gene",
        "variant",
        "genetic_ancestry_group",
        "allele_frequency"
    }

    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    if not df["allele_frequency"].between(0, 1).all():
        raise ValueError("Allele frequencies must be between 0 and 1")

    return df


if __name__ == "__main__":
    df = load_allele_frequencies()
    print("Loaded allele frequency data:")
    print(df)

