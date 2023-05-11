from db.repositories.base import BaseSession

# открытие транзакции
from db.repositories.cities import CityRepository
from db.tables import City
from db.utils.decorators.error_handler import orm_error_handler
from dto.filters.paginate import BasePaginateDTO


class CityService:
    def __init__(
        self,
        session: BaseSession,
        city_repo: CityRepository,
    ):
        self.session = session
        self.city_repo = city_repo

    @orm_error_handler
    async def get_one(self, id_: int) -> City:
        async with self.session.transaction():
            city = await self.city_repo.get_one(
                id_=id_,
            )
            return city

    @orm_error_handler
    async def get_all(
        self,
    ):
        async with self.session.transaction():
            cities = await self.city_repo.get_all()
            return cities
