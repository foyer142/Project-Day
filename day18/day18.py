
class UserService:
    def __init__(self):
        self.users = []

    def add_user(self, user: dict) -> None:
        self.users.append(user)

    def get_all_users(self) -> list[dict]:
        return self.users

    def get_active_users(self) -> list[dict]:
        return [user for user in self.users if user['is_active']]

    def get_adult_users(self) -> list[dict]:
        return [user for user in self.users if user['age']>=18]

    def find_by_city(self, city: str) -> list[dict]:
        return [user for user in self.users if user['city']==city]

    def find_by_email(self, email: str) -> dict | None:
        return next((user for user in self.users if user['email']==email),None)

    def deactivate_user(self, email: str) -> bool:
        for user in self.users:
            if user['email']==email:
                user['is_active'] = False
                return True
        return False
    
def main():
    service = UserService()

    service.add_user({
        "name": "Bulat",
        "age": 20,
        "email": "bulat@mail.com",
        "city": "Tomsk",
        "is_active": True,
    })

    service.add_user({
        "name": "Anna",
        "age": 17,
        "email": "anna@mail.com",
        "city": "Moscow",
        "is_active": True,
    })

    service.add_user({
        "name": "Ivan",
        "age": 25,
        "email": "ivan@mail.com",
        "city": "Tomsk",
        "is_active": False,
    })

    print(service.get_all_users())
    print(service.get_active_users())
    print(service.get_adult_users())
    print(service.find_by_city("Tomsk"))
    print(service.find_by_email("anna@mail.com"))
    print(service.deactivate_user("anna@mail.com"))
    print(service.find_by_email("anna@mail.com"))
    print(service.deactivate_user("missing@mail.com"))




if __name__=='__main__':
    main()