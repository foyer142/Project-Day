
def get_users_by_city(users: list[dict], city: str) -> list[dict]:
    return [user for user in users if user['city']==city]

def get_users_with_email(users: list[dict]) -> list[dict]:
    return [user for user in users if user['contacts'].get('email','No email') != 'No email']

def add_status_to_users(users: list[dict]) -> list[dict]:
    for user in users:
        if user['age'] >= 18:
            user.update({'status':'adult'})
        else:
            user.update({'status':'minor'})
    return users


def group_users_by_city(users: list[dict]) -> dict:
    grouped_users = {}

    for user in users:
        city = user["city"]

        if city not in grouped_users:
            grouped_users[city] = []

        grouped_users[city].append(user['name'])

    return grouped_users




users = [
    {
        "name": "Bulat",
        "age": 20,
        "city": "Tomsk",
        "contacts": {"email": "bulat@example.com"},
    },
    {
        "name": "Anna",
        "age": 17,
        "city": "Moscow",
        "contacts": {},
    },
    {
        "name": "Ivan",
        "age": 22,
        "city": "Tomsk",
        "contacts": {"email": "ivan@example.com"},
    },
]


print(get_users_by_city(users,'Tomsk'),'\n')

print(get_users_with_email(users),'\n')

print(add_status_to_users(users),'\n')

print(group_users_by_city(users),'\n')