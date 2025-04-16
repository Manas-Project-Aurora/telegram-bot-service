from enum import StrEnum


class VacancyStatus(StrEnum):
    ACTIVE = "active"
    PENDING = "pending"
    SUSPENDED = "suspended"
    REJECTED = "rejected"
