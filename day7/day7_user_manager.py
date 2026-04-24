import json


def save_users(filename: str, users: list[dict]) -> None:
    with open(filename,'w',encoding='utf-8') as file:
        json.dump(users, file, ensure_ascii=False, indent=4)

def load_users(filename: str) -> list[dict]:
        with open(filename,'r',encoding='utf-8') as file:
            load_users = json.load(file)
        return load_users

def get_adult_users(users: list[dict]) -> list[dict]:
    is_adult_users = []
    for user in users:
        if user['age'] >= 18:
            is_adult_users.append(user) 
    return is_adult_users

def get_users_by_city(users: list[dict], city: str) -> list[dict]:
    users_in_city = []
    for user in users:
        if user['city'] == city:
            users_in_city.append(user)
    return users_in_city

def get_unique_skills(users: list[dict]) -> list[str]:
    uniqe_skills_users = []
    for user in users:
        for skill in user['skills']:
            if skill not in uniqe_skills_users:
                uniqe_skills_users.append(skill)
    return uniqe_skills_users

def format_user(user: dict) -> str:
    return f'{user['name']}, {user['age']} years old, {user['city']}, skills: {', '.join(user['skills'])}'

def print_users(users: list[dict]) -> None:
    for user in users:
        print(format_user(user))


users = [
    {"name": "Bulat", "age": 20, "city": "Tomsk", "skills": ["Python", "Git"]},
    {"name": "Anna", "age": 17, "city": "Moscow", "skills": ["HTML", "CSS"]},
    {"name": "Ivan", "age": 22, "city": "Tomsk", "skills": ["FastAPI", "PostgreSQL"]},
    {"name": "Mira", "age": 19, "city": "Kazan", "skills": ["Python", "Docker"]},
    {"name": "Dias", "age": 19, "city": "Ust-Kamenogorsk", "skills": ["Python", "Java"]},
]


save_users("day7/users.json", users)

loaded_users = load_users("day7/users.json")

adult_users = get_adult_users(loaded_users)
tomsk_users = get_users_by_city(loaded_users, "Tomsk")
unique_skills = get_unique_skills(loaded_users)

print("All users:")
print_users(loaded_users)

print("Adult users:")
print_users(adult_users)

print("Tomsk users:")
print_users(tomsk_users)

print("Unique skills:")
print(unique_skills)
