import pathlib
import tomllib
from dataclasses import dataclass
from typing import Final

__all__ = ('Config', 'load_config_from_file', 'SRC_DIR', 'CONFIG_FILE_PATH')

SRC_DIR = pathlib.Path(__file__).parent
CONFIG_FILE_PATH: Final = SRC_DIR.parent / 'config.toml'


@dataclass(frozen=True, slots=True)
class Config:
    telegram_bot_token: str
    api_base_url: str
    website_base_url : str
    vacancy_channel_chat_id: int


def load_config_from_file() -> Config:
    """Загружает конфигурацию из TOML файла."""
    config_toml = CONFIG_FILE_PATH.read_text(encoding='utf-8')
    config = tomllib.loads(config_toml)

    return Config(
        telegram_bot_token=config['telegram_bot']['token'],
        api_base_url=config['api']['base_url'],
        website_base_url=config['website']['base_url'],
        vacancy_channel_chat_id=config['vacancy_channel']['chat_id']

    )