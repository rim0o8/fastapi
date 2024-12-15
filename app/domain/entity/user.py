from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    id: int
    name: str
    email: str
    created_at: datetime = datetime.now()

    def validate_name(self) -> bool:
        """名前の妥当性検証"""
        return len(self.name) >= 2

    def validate_email(self) -> bool:
        """メールアドレスの妥当性検証"""
        return "@" in self.email

    def change_name(self, new_name: str) -> None:
        """名前の変更"""
        if len(new_name) < 2:
            raise ValueError("名前は2文字以上必要です")
        self.name = new_name

    @property
    def display_name(self) -> str:
        """表示用の名前を取得"""
        return f"{self.name} <{self.email}>"
