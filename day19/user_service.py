
class UserService:
    def __init__(self):
        self.users = []

    def add_user(self, name: str, age: int, city: str, email: str) -> None:
        self.users.append({
            "name": name,
            "age": age,
            "city": city,
            "email": email,
        })

    def get_all_users(self) -> list[dict]:
        return self.users

    def find_by_city(self, city: str) -> list[dict]:
        return [user for user in self.users if user['city']==city]

    def find_by_email(self, email: str) -> dict | None:
        return next((user for user in self.users if user['email']==email),None)
