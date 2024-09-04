from pydantic import BaseModel, ConfigDict


class Pagination:
    limit: int
    currentPage: int
    totalPages: int
    totalItems: int