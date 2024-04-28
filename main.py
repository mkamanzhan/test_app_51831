import uvicorn

from src.configs import configs
from src.main import get_app

if __name__ == "__main__":
    uvicorn.run(
        get_app(),
        host=configs.fast_api.host,
        port=configs.fast_api.port,
    )
