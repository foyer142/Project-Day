import day11

def normalize_user(user: dict) -> dict:
    user.update({'name' : day11.normalize_name(user['name']), 'status' : day11.get_user_status(user['age'])})
    return user

def normalize_users(users: list[dict]) -> list[dict]:
    return [normalize_user(user) for user in users]

def get_active_users(users: list[dict]) -> list[dict]:
    return [user for user in users if day11.is_active(user)]

def get_admin_users(users: list[dict]) -> list[dict]:
    return [user for user in users if day11.is_admin(user)]

def get_users_with_admin_access(users: list[dict]) -> list[dict]:
    return [user for user in users if day11.is_admin(user) and day11.is_active(user)]

def format_user(user: dict) -> str:
    normalize_user(user)
    if user['is_active']:
        active_status = "active"
    else:
        active_status = "inactive"
    return f'{user['name']} | {user['status']} | {user['city']} | {user['role']} | {active_status}'

users = [
    {"name": "  bulat  ", "age": 20, "city": "Tomsk", "role": "admin", "is_active": True},
    {"name": "anna", "age": 17, "city": "Moscow", "role": "user", "is_active": True},
    {"name": "ivan", "age": 22, "city": "Tomsk", "role": "admin", "is_active": False},
]


print(normalize_users(users), "\n")
print(get_active_users(users), "\n")
print(get_admin_users(users), "\n")
print(get_users_with_admin_access(users), "\n")
print(format_user(users[0]))
