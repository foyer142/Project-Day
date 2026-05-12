
import json

def load_users(filename: str) -> list[dict]:
    try:
        with open(filename, 'r',encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    
def save_users(filename: str, users: list[dict]) -> None:
    with open(filename,'w',encoding='utf-8') as file:
        json.dump(users,file,indent=4,ensure_ascii=False)
