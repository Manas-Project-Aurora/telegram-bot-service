from bot.providers.http_client import ApiGatewayHttpClient
from bot.services.api_gateway import ApiGateway


def api_gateway_provider(
    http_client: ApiGatewayHttpClient,
) -> ApiGateway:
    return ApiGateway(http_client=http_client)
