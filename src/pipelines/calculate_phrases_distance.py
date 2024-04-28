from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count

import polars as pl
from loguru import logger

from src.configs import configs
from src.models.vectors_model import vector_model


def _load_model() -> None:
    if not vector_model.is_initialized():
        vector_model.init_model(configs.data.vectors_path)


def _read_csv(path: str) -> pl.DataFrame:
    return pl.read_csv(path)


def _join_pairs(df: pl.DataFrame) -> pl.DataFrame:
    return df.select("phrases").join(df.select("phrases"), how="cross")


def _calc_distances(
    data: list[tuple[str, str]],
) -> list[tuple[str, str, float]]:
    _load_model()

    result = []
    for row in data:
        result.append(
            (
                row[0],
                row[1],
                vector_model.calculate_distance(row[0], row[1]),
            )
        )
    return result


def _split_into_chunks(df: pl.DataFrame) -> list:
    chunks_count = min(cpu_count(), len(df))
    chunks = [[] for _ in range(chunks_count)]
    chunk_index = 0
    for i in df.iter_rows():
        chunks[chunk_index].append(i)
        chunk_index = (chunk_index + 1) % chunks_count
    return chunks


def _run_calc_split_by_processes(df: pl.DataFrame) -> pl.DataFrame:
    result = []
    chunks = _split_into_chunks(df)

    with ProcessPoolExecutor() as executor:
        logger.info("Calculating distances...")
        for score in executor.map(_calc_distances, chunks):
            result.extend(score)
        executor.shutdown(wait=True)

    return pl.DataFrame(result, schema=("phrase1", "phrase2", "distance"))


def _calc_distance(df: pl.DataFrame) -> pl.DataFrame:
    result = []
    for row in df.iter_rows():
        result.append(
            (
                row[0],
                row[1],
                vector_model.calculate_distance(row[0], row[1]),
            )
        )
    return pl.DataFrame(result, schema=("phrase1", "phrase2", "distance"))


def _save_result(df: pl.DataFrame, target_path: str) -> None:
    df.write_csv(target_path)


def run_pipeline(phrases_csv_path: str, target_path: str) -> None:
    _load_model()
    df = _read_csv(phrases_csv_path)
    df = _join_pairs(df)

    if configs.data.use_multiprocessing:
        df = _run_calc_split_by_processes(df)
    else:
        df = _calc_distance(df)

    _save_result(df, target_path)
