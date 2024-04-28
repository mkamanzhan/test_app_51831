import polars as pl


def clean_phrases(
    source_path: str,
    target_path: str,
) -> None:
    df = pl.read_csv(
        source_path,
        ignore_errors=True,
    )

    df = df.rename(lambda x: x.lower())
    df = df.with_columns(pl.col("phrases").str.to_lowercase())
    df = df.with_columns(pl.col("phrases").str.strip_chars())
    df = df.with_columns(pl.col("phrases").str.replace_all("[?,`,']", ""))
    df = df.drop_nulls()
    df = df.unique()

    df.write_csv(target_path)


def run_pipeline() -> None:
    clean_phrases(
        source_path="data/raw/phrases.csv",
        target_path="data/cleaned/phrases.csv",
    )
