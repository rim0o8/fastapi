from domain.entity.user import User
from domain.repository.user import UserRepository


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users: list[User] = [
            User(id=1, name="田中太郎", email="tanaka@example.com"),
            User(id=2, name="山田花子", email="yamada@example.com"),
        ]

    def get_users(self) -> list[User]:
        return self.users

    def get_user(self, user_id: int) -> User:
        user = next((u for u in self.users if u.id == user_id), None)
        if not user:
            raise ValueError("ユーザーが見つかりません")
        return user

    def create_user(self, user: User) -> User:
        self.users.append(user)
        return user
