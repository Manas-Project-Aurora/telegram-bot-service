from dishka import Provider, Scope, provide

from providers.http_client import ApiGatewayHttpClient
from services.api_gateway import ApiGateway


class ApiGatewayProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_api_gateway(
            self,
            http_client: ApiGatewayHttpClient,
    ) -> ApiGateway:
        return ApiGateway(http_client=http_client)
