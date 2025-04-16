import datetime

from pydantic import BaseModel

from enums.vacancy_salary_types import VacancySalaryType
from enums.vacancy_statuses import VacancyStatus
from enums.vacancy_types import VacancyType
from models.pagination import Pagination


class Vacancy(BaseModel):
    id: int
    title: str
    organization_id: int
    organization_name: str
    description: str | None
    salary_from: int | None
    salary_to: int | None
    status: VacancyStatus
    type: VacancyType
    salary_type: VacancySalaryType
    created_at: datetime.datetime
    updated_at: datetime.datetime


class VacancyPage(BaseModel):
    vacancies: list[Vacancy]
    pagination: Pagination
