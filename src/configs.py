from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

from src.core.logging.enums import LogLevel


class _Logging(BaseModel):
    level: LogLevel = LogLevel.info


class _FastApiConfigs(BaseSettings):
    host: str = "localhost"
    port: int = 8000
    debug: bool = False


class _ModelData(BaseModel):
    vectors_path: str = "data/vectors.csv"
    use_multiprocessing: bool = False
    distances_path: str = "data/distances.csv"


class Configs(BaseSettings):
    title: str = "Galatix Test App"

    fast_api: _FastApiConfigs = _FastApiConfigs()
    logging: _Logging = _Logging()

    data: _ModelData = _ModelData()
    redis_url: str = "redis://localhost:6379/0"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="__",
    )


configs = Configs()
