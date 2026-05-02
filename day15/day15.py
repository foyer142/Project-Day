import json

def safe_divide(a: int, b: int) -> float | None:
    try:
        result = a/b
        return result
    except ZeroDivisionError:
        return None

def parse_age(value: str) -> int | None:
    try:
        return int(value)
    except ValueError:
        return None
    
def get_user_age(user: dict) -> int | None:
    try:
        user_age = user['age']
        return user_age
    except KeyError:
        return None
    
def read_file(filename: str) -> str:
    try:
        with open(filename, 'r',encoding='utf-8') as file:
            load_file = file.read()
        return load_file
    
    except FileNotFoundError:
        return ""


def parse_json(text: str) -> dict | list | None:
    try:
        data = json.loads(text)
        return data
    except ValueError:
        return None
    
def get_first_item(items: list) -> object | None:
    try:
        return items[0]
    except IndexError:
        return None

def main():
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))

    print(parse_age("20"))
    print(parse_age("abc"))

    print(get_user_age({"name": "Bulat", "age": 20}))
    print(get_user_age({"name": "Anna"}))

    print(read_file("missing.txt"))

    print(parse_json('{"name": "Bulat"}'))
    print(parse_json("{bad json}"))

    print(get_first_item([1, 2, 3]))
    print(get_first_item([]))


if __name__ == '__main__':
    main()
    
