from datetime import UTC, datetime


def utc_now() -> datetime:
    return datetime.now(UTC)


def utc_now_timestamp() -> float:
    return utc_now().timestamp()
