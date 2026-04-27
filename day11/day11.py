
def is_adult(age: int) -> bool:
    return age >= 18

def get_user_status(age: int) -> str:
    if is_adult(age):
        return 'adult'
    return 'minor'

def is_old(age : int) -> bool:
    return age >= 60

def calculate_discount(age: int, is_student: bool) -> int:
    if not is_adult(age):
        return 20
    if is_student:
        return 15
    if is_old(age):
        return 10
    return 0

def normalize_name(name: str) -> str:
    return name.strip().title()

def build_user(name: str, age: int, city: str) -> dict:
    user = {
        'name' : normalize_name(name),
        'age' : age,
        'city' : city,
        'status' : get_user_status(age)
    }
    return user

def is_admin(user: dict) -> bool:
    return user["role"] == "admin"
    
def is_active(user: dict) -> bool:
    return user["is_active"]

def can_access_admin_panel(user: dict) -> bool:
    return is_admin(user) and is_active(user)