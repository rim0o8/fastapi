from domain.entity.user import User
from domain.repository.user import UserRepository


class UserUseCase:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    def get_users(self) -> list[User]:
        return self._repository.get_users()

    def get_user(self, user_id: int) -> User:
        return self._repository.get_user(user_id)

    def create_user(self, name: str, email: str) -> User:
        # ビジネスロジックのバリデーション
        if len(name) < 2:
            raise ValueError("名前は2文字以上必要です")

        # メールアドレスの重複チェックなどのビジネスルール
        if any(u.email == email for u in self._repository.get_users()):
            raise ValueError("このメールアドレスは既に使用されています")

        # 新しいユーザーの作成
        new_user = User(
            id=len(self._repository.get_users()) + 1, name=name, email=email
        )
        return self._repository.create_user(new_user)
