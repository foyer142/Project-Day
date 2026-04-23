def get_user_name(user: dict) -> str:
    return user['name']

def add_is_adult(user: dict) -> dict:
    Flag = False
    if user['age'] >= 18:
        Flag = True
    user['is_adult'] = Flag
    return  user

def count_total_skills(users: list[dict]) -> int:
    cnt = 0
    for i in range(len(users)):
        cnt += len(users[i]['skills'])
    return cnt

def find_user_by_city(users: list[dict], city: str) -> list[dict]:
    all_users_in_city = []
    for i in range(len(users)):
        if users[i]['city'] == city:
            all_users_in_city.append(users[i])
    return  all_users_in_city


user = {
    "name": "Bulat",
    "age": 20,
    "skills": ["Python", "HTML"],
}

users = [
    {"name": "Bulat", "age": 20,"skills": ["Python", "CSS"],'city':'Moskva'},
    {"name": "Anna", "age": 17,"skills": ["Python", "HTML","CSS"],'city':'Tomsk'},
    {"name": "Asap", "age": 17,"skills": ["Python", "HTML"],'city':'Tomsk'},
    {"name": "Rassol", "age": 17,"skills": ["Python"],'city':'Tomsk'},
]


print(get_user_name(user))

print(add_is_adult(user))

print(count_total_skills(users))

print(find_user_by_city(users,'Tomsk'))
