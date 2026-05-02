
def get_active_users(users: list[dict]) -> list[dict]:
    active_users = []
    for user in users:
        if user['is_active']:
            active_users.append(user)
    return active_users

def get_adult_users(users: list[dict]) -> list[dict]:
    adult_users = []
    for user in users:
        if user['age']>= 18:
            adult_users.append(user)
    return adult_users

def get_users_by_city(users: list[dict], city: str) -> list[dict]:
    user_in_city = []
    for user in users:
        if user['city'] == city:
            user_in_city.append(user)
    return user_in_city