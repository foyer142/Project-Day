
def get_user_city(user: dict) -> str:
    return user.get('city','Unknown')

def update_user_email(user: dict, email: str) -> dict:
    user['contacts'].update({'email' : email})
    return user

def get_user_keys(user: dict) -> list[str]:
    return [key for key in user.keys()]

def get_user_values(user: dict) -> list:
    return [value for value in user.values()]

def format_user_fields(user: dict) -> list[str]:
    format_user = []
    for key,value in user.items():
        format_user.append(f'{key} : {value}')
    return format_user

def get_contact_email(user: dict) -> str:
    return user['contacts'].get('email',"No email")


user = {
    "name": "Bulat",
    "age": 20,
    "city": "Tomsk",
    "contacts": {
        "email": "bulat@example.com",
        "phone": "+70000000000",
    },
}


user_without_city = {
    "name": "Anna",
    "age": 17,
    "contacts": {},
}

print(get_user_city(user_without_city))

print(update_user_email(user,"reveri@example.com"),'\n')

print(get_user_keys(user),'\n')

print(get_user_values(user),'\n')

print(format_user_fields(user),'\n')

print(get_contact_email(user_without_city))