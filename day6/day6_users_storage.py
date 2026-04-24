import json


def save_users(filename: str, users: list[dict]) -> None:
    with open(f'{filename}.json','w',encoding='utf-8') as file:
        json.dump(users,file, ensure_ascii=False, indent=4)

def load_users(filename: str) -> list[dict]:
    with open(f'{filename}.json','r',encoding='utf-8') as file:
        read_json = json.load(file)
    return read_json

def get_adult_users(users: list[dict]) -> list[dict]:
    adult_users = []
    for user in users:
        if user['age'] >= 18:
            adult_users.append(user)
    return adult_users

def get_users_by_city(users: list[dict], city: str) -> list[dict]:
    in_city = []
    for user in users:
        if user['city'] == city:
            in_city.append(user)
    return in_city

users = [
    {"name": "Bulat", "age": 20, "city": "Tomsk"},
    {"name": "Anna", "age": 17, "city": "Moscow"},
    {"name": "Ivan", "age": 22, "city": "Tomsk"},
]

save_users("day6/users", users)

loaded_users = load_users("day6/users")
print(loaded_users,'\n')

print(get_adult_users(loaded_users),'\n')

moscow_users = get_users_by_city(loaded_users, "Moscow")
print(moscow_users,'\n')


