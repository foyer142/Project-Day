
class UserAccount:
    def __init__(self,name,email,password,is_active):
        self.name = name
        self.email = email
        self.password = password
        self.is_active = is_active

    def check_password(self,password: str) -> bool:
        return self.password == password
    
    def deactivate(self) -> None:
        self.is_active = False
        
    def activate(self) -> None:
        self.is_active = True

    def can_access(self) -> bool:
        return self.is_active
    
    def get_public_profile(self) -> dict:
        return {
            'name' : self.name,
            'email' : self.email,
            'is_active' : self.is_active 
        }

def main():
    user = UserAccount("Bulat", "bulat@mail.com", "12345", True)

    print(user.check_password("12345"))
    print(user.check_password("wrong"))

    print(user.can_access())
    user.deactivate()
    print(user.can_access())
    user.activate()
    print(user.can_access())

    print(user.get_public_profile())

if __name__ == '__main__':
    main()