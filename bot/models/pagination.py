from pydantic import BaseModel


class Pagination(BaseModel):
    total_count: int
    skipped_count: int
    taken_count: int
