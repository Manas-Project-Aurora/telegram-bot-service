from dataclasses import dataclass

from enums.vacancy_statuses import VacancyStatus
from models.users import UserPage
from models.vacancies import VacancyPage
from providers.http_client import ApiGatewayHttpClient


@dataclass(frozen=True, slots=True, kw_only=True)
class ApiGateway:
    http_client: ApiGatewayHttpClient

    async def get_admins(self) -> UserPage:
        url = "/v1/users/"
        query_params: dict = {"is_admin": True}
        response = await self.http_client.get(url, params=query_params)
        return UserPage.model_validate_json(response.text)

    async def get_pending_vacancies(
        self,
        *,
        take: int | None = None,
        skip: int | None = None,
    ) -> VacancyPage:
        url = "/v1/vacancies/"
        query_params: dict = {"statuses": (VacancyStatus.PENDING)}
        if take is not None:
            query_params["take"] = take
        if skip is not None:
            query_params["skip"] = skip
        response = await self.http_client.get(url, params=query_params)
        return VacancyPage.model_validate_json(response.text)

    async def reject_vacancy(self, vacancy_id: int) -> None:
        url = f"/v1/vacancies/{vacancy_id}/reject/"
        await self.http_client.post(url)

    async def approve_vacancy(self, vacancy_id: int) -> None:
        url = f"/v1/vacancies/{vacancy_id}/approve/"
        await self.http_client.post(url)
