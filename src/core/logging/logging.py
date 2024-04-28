import sys

from loguru import logger

from src.core.logging.enums import LogLevel


def init_logger(level: LogLevel) -> None:
    level_str = level.value.upper()

    logger.remove()
    logger.add(
        sys.stdout,
        format=(
            "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
            "<level>{level: <8}</level> | "
            "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
            "<level>{message}</level>"
        ),
        level=level_str,
        colorize=True,
    )

    logger.info("Logger initialized")
