
class UserService:
    def __init__(self,users: list[dict] | None = None):
        self.users = users or []

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
        return [user for user in self.users if user['city'].lower() == city.lower()]

    def find_by_email(self, email: str) -> dict | None:
        return next((user for user in self.users if user['email'].lower() == email.lower()),None)

    def delete_by_email(self, email: str) -> bool:
        user = self.find_by_email(email)
        if user is None:
            return False 
        self.users.remove(user)
        return True