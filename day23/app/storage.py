from pathlib import Path
import json
from custom_types import UserDict

def load_users(filename: str) -> list[UserDict]:
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
    
def save_users(filename: Path, users: list[UserDict]) -> None:
    with open(filename,'w',encoding='utf-8') as file:
        json.dump(users,file,indent=4,ensure_ascii=False)
