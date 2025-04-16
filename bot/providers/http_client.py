from typing import NewType

import httpx
from dishka import Provider, provide, Scope

from config import Config

ApiGatewayHttpClient = NewType("ApiGatewayHttpClient", httpx.AsyncClient)


class HttpClientProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def provide_http_client(
            self,
            config: Config,
    ) -> ApiGatewayHttpClient:
        return ApiGatewayHttpClient(
            httpx.AsyncClient(base_url=config.api_base_url)
        )
