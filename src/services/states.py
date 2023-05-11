from typing import Sequence

from db.repositories.base import BaseSession
from db.repositories.states import StateRepository
from db.tables import State
from db.utils.decorators.error_handler import orm_error_handler


class StateService:
    def __init__(
        self,
        session: BaseSession,
        state_repo: StateRepository,
    ):
        self.session = session
        self.state_repo = state_repo

    @orm_error_handler
    async def get_one(self, id_: int) -> State:
        async with self.session.transaction():
            state = await self.state_repo.get_one(
                id_=id_,
            )
            return state

    @orm_error_handler
    async def get_all(
        self,
    ) -> Sequence[State]:
        async with self.session.transaction():
            states = await self.state_repo.get_all()
            return states
