
import utils

def normalize_user(user: dict) -> dict:
    user.update({'name' : utils.normalize_name(user['name']), 'status' : utils.get_status(user['age'])})
    return user

def normalize_users(users: list[dict]) -> list[dict]:
    return [normalize_user(user) for user in  users]

def get_adult_users(users: list[dict]) -> list[dict]:
    return [user for user in users if utils.is_adult(user['age'])]

def format_user(user: dict) -> str:
    user = normalize_user(user)
    return f'{user['name']} | {user['status']} | {user['city']}'

def main() -> None:
    user = {"name": "  bulat  ", "age": 20, "city": "Tomsk"}

    users = [
    {"name": "  bulat  ", "age": 20, "city": "Tomsk"},
    {"name": "anna", "age": 17, "city": "Moscow"},
    {"name": "ivan", "age": 22, "city": "Tomsk"},
    ]

    print(normalize_user(user),'\n')

    print(normalize_users(users),'\n')

    print(get_adult_users(users),'\n')

    print(format_user(user),'\n')




if __name__ == '__main__':
    main()