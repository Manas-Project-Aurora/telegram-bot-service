from dishka import Provider, provide, Scope

from config import Config, load_config_from_file


class ConfigProvider(Provider):
    @provide(scope=Scope.APP)
    async def provide_config(self) -> Config:
        return load_config_from_file()
