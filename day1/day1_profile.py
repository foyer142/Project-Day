
def is_adult(age: int) -> str:
    if age >= 18:
        txt = 'Access granted'
    else:
        txt = 'Access denied'
    return txt

def print_card(user: dict) ->str:
    return f'User: name - {user['name']}, age - {user['age']}, city - {user['city']}, like language - {user['favorite_language']}'


user = {
    "name": "Bulat",
    "age": 20,
    "city": "Tomsk",
    "favorite_language": "Python",
}

print(print_card(user))
print(is_adult(user['age']))
