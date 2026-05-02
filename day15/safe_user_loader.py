import json

def load_users(filename: str) -> list[dict]:
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
        return []
    
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def get_user_names(users: list[dict]) -> list[str]:
    users_with_name = []
    for user in users:
        try:
            users_with_name.append(user['name'])
        except KeyError:
            pass
    return users_with_name

