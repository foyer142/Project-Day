import json


def write_text_to_file(filename: str, text: str) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
    

def read_text_from_file(filename: str) -> str:
    with open(filename, 'r',encoding='utf-8') as file:
        read_file = file.read()
    return read_file

def save_user_to_json(filename: str, user: dict) -> None:
    with open(f'{filename}.json', 'w',encoding='utf-8') as file:
        json.dump(user,file, sort_keys=True, ensure_ascii=False, indent=4)

def load_user_from_json(filename: str) -> dict:
    with open(f'{filename}.json','r',encoding='utf-8') as file:
        reading_json = json.load(file)
    return  reading_json

write_text_to_file('day6/note.txt','Филитек myu 1001010010') 

print(read_text_from_file('day6/note.txt'))

users = {"name": "Bulat", "age": 20, "city": "Tomsk"}
save_user_to_json('day6/user',users)


print(load_user_from_json('day6/user'))
