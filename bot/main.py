import asyncio
import logging
import sys
from typing import Union

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dishka import make_async_container, Scope
from dishka.integrations.aiogram import setup_dishka

import handlers.start
from config import Config
from providers.api_gateway import ApiGatewayProvider
from providers.config import ConfigProvider
from providers.http_client import HttpClientProvider
from services.api_gateway import ApiGateway


async def main() -> None:
    container = make_async_container(
        ConfigProvider(),
        HttpClientProvider(),
        ApiGatewayProvider(),
    )
    config = await container.get(Config)

    bot = Bot(
        token=config.telegram_bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    dp = Dispatcher()
    dp.include_router(handlers.start.router)

    setup_dishka(container=container, router=dp, auto_inject=True)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
