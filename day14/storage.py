import json

def load_users(filename: str) -> list[dict]:
    with open(filename,'r',encoding='utf-8') as file:
        users = json.load(file)
    return users