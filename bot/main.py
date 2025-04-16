import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dishka import Provider, Scope, make_async_container
from dishka.integrations.aiogram import setup_dishka

from bot.providers.api_gateway import api_gateway_provider
from bot.services.api_gateway import ApiGateway
import handlers.start
from providers.http_client import (
    ApiGatewayHttpClient,
    api_gateway_http_client_provider,
)
from config import load_config_from_file, Config


async def main() -> None:
    provider = Provider(scope=Scope.APP)
    provider.provide(load_config_from_file, provides=Config, scope=Scope.APP)

    provider.provide(
        api_gateway_http_client_provider,
        provides=ApiGatewayHttpClient,
        scope=Scope.REQUEST,
    )
    provider.provide(
        api_gateway_provider,
        provides=ApiGateway,
        scope=Scope.REQUEST,
    )

    container = make_async_container(provider)

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
