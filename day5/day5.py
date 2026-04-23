
def normalize_text(text: str) -> str:
    return  text.strip().title()

def split_sentences(text: str) -> list[str]:
    sentences = text.split('.')
    return [sentence.strip() for sentence in sentences if sentence.strip()] 

def count_characters_without_spaces(text: str) -> int:
    cnt = 0
    for _ in text:
        if _ != ' ':
            cnt += 1
    return cnt

def build_full_name(first_name: str, last_name: str) -> str:
    return normalize_text(first_name) + ' ' + normalize_text(last_name)

users = [
    {"name": "  bulat  ", "age": 20, "city": "Tomsk"},
    {"name": "anna", "age": 17, "city": "Moscow"},
    {"name": "ivan", "age": 22, "city": "Tomsk"},
]

text = "Hello. How are you. I'm fine."

print(normalize_text(users[0]['name']))

print(split_sentences(text))

print(count_characters_without_spaces(text))

print(build_full_name(" ivan", "Petrov"))


