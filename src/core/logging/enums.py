from src.core.enums import CaseInsensitiveStrEnum


class LogLevel(CaseInsensitiveStrEnum):
    debug = "debug"
    info = "info"
    warning = "warning"
    error = "error"
    critical = "critical"
