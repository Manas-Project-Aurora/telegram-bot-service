import httpx
from config import load_config_from_file

# Загружаем конфигурацию
config = load_config_from_file()

def get_http_client() -> httpx.AsyncClient:
    """Создает и возвращает асинхронный HTTP-клиент с базовым URL API."""
    return httpx.AsyncClient(base_url=config.api_base_url)