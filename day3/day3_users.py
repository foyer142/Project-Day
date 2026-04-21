def get_name_users(users: list[dict]) -> list:
    name_users = []
    for user in users:
        name_users.append(user['name'])
    return name_users

def is_adult_users(users: list[dict]) -> list:
    adult_users = []
    for user in users:      
        if user['age'] >= 18:
            adult_users.append(user['name'])
    return adult_users

def count_skills_users(users: list[dict]) -> int:
    cnt = 0
    for user in users:
        cnt += len(user['skills'])
    return cnt


def find_user_in_city(users: list[dict],city:str) -> list:
    city_residents = []
    for user in users:
        if user['city'] == city:
            city_residents.append(user['name'])
    return city_residents


users = [
    {"name": "Bulat", "age": 20, "city": "Tomsk", "skills": ["Python", "Git"]},
    {"name": "Anna", "age": 17, "city": "Moscow", "skills": ["HTML", "CSS"]},
    {"name": "Ivan", "age": 22, "city": "Tomsk", "skills": ["FastAPI"]},
]


print(get_name_users(users))

print(is_adult_users(users))

print(count_skills_users(users))

print(find_user_in_city(users,'Tomsk'))