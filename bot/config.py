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


def load_config_from_file(config_file_path: pathlib.Path = CONFIG_FILE_PATH) -> Config:
    """Загружает конфигурацию из TOML файла."""
    config_toml = config_file_path.read_text(encoding='utf-8')
    config = tomllib.loads(config_toml)

    return Config(
        telegram_bot_token=config['telegram_bot']['token'],
    )
