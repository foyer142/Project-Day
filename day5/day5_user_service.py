def normalize_text(text: str) -> str:
    return  text.strip().title()

def is_adult_users(users : list[dict]) -> list[dict]:
    adult_users = []
    for user in users:
        if user['age'] >= 18:
            adult_users.append(user)
    return adult_users

def name_users(users : list[dict]) -> list[str]:
    names = []
    for user in users:
        names.append(normalize_text(user['name'])) 
    return names

def beautiful_string_user(user : dict ) -> str:
    beautiful_string = []
    for i in user:
        beautiful_string.append(normalize_text(i) + ' - ' + normalize_text(str(user[i])))
    return ', '.join(beautiful_string)

users = [
    {"name": "  bulat  ", "age": 20, "city": "Tomsk"},
    {"name": "anna", "age": 17, "city": "Moscow"},
    {"name": "ivan", "age": 22, "city": "Tomsk"},
]

print(is_adult_users(users),'\n')

print(name_users(users),'\n')

print(beautiful_string_user(users[0]))