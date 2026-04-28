def normalize_name(name: str) -> str:
    return name.strip().title()

def is_adult(age: int) -> bool:
    return age >= 18

def get_status(age: int) -> str:
    if is_adult(age):
        return 'adult'
    return 'minor'