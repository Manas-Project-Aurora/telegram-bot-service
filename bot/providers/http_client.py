from typing import NewType

import httpx

from config import Config


ApiGatewayHttpClient = NewType("ApiGatewayHttpClient", httpx.AsyncClient)


async def api_gateway_http_client_provider(
    config: Config,
) -> ApiGatewayHttpClient:
    return ApiGatewayHttpClient(
        httpx.AsyncClient(
            base_url=config.api_base_url,
        )
    )
