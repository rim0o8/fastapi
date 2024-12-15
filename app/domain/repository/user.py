from abc import ABC, abstractmethod

from domain.entity.user import User


class UserRepository(ABC):
    @abstractmethod
    def get_users(self) -> list[User]:
        pass

    @abstractmethod
    def get_user(self, user_id: int) -> User:
        pass

    @abstractmethod
    def create_user(self, user: User) -> User:
        pass
