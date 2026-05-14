from custom_types import UserDict


class UserService:
    def __init__(self,users: list[UserDict] | None = None):
        self.users = users or []

    def add_user(self, user : UserDict) -> None:
        self.users.append(user)

    def get_all_users(self) -> list[UserDict]:
        return self.users

    def find_by_city(self, city: str) -> list[UserDict]:
        return [user for user in self.users if user['city'].lower() == city.lower()]

    def find_by_email(self, email: str) -> UserDict | None:
        return next((user for user in self.users if user['email'] == email),None)

    def delete_by_email(self, email: str) -> bool:
        user = self.find_by_email(email)
        if user is None:
            return False 
        self.users.remove(user)
        return True