
def is_non_empty_string(value: object) -> bool:
    return isinstance(value,str) and value.strip() != ''

def is_valid_age(age: object) -> bool:
    return isinstance(age,int) and (0<=int(age)<=120)

def has_required_fields(data: dict, fields: list[str]) -> bool:
    return all(field in data for field in fields)

def is_valid_email(email: object) -> bool:
    return isinstance(email,str) and '@' in str(email) and '.' in str(email) and str(email.strip()) != ''

def validate_user(user: dict) -> list[str]:
    list_errors = []
    #cheсk name
    if 'name' not in user:
        list_errors.append('name is required')
    elif not is_non_empty_string(user['name']):
        list_errors.append("name must be non-empty string")
    #age
    if 'age' not in user:
        list_errors.append('age is required')
    elif not  is_valid_age(user['age']):
        list_errors.append('age must be integer from 0 to 120')
    #email
    if 'email' not in user:
        list_errors.append('email is required')
    elif not  is_valid_email(user['email']):
        list_errors.append('email is invalid')
    
    return list_errors 

def is_valid_user(user: dict) -> bool:
    return validate_user(user) == []


def main():
    valid_user = {
        "name": "Bulat",
        "age": 20,
        "email": "bulat@mail.com"
    }

    invalid_user = {
        "name": "   ",
        "age": "twenty",
        "email": "wrong-email"
    }

    missing_user = {
        "city": "Tomsk"
    }

    print(validate_user(valid_user))
    print(is_valid_user(valid_user))

    print(validate_user(invalid_user))
    print(is_valid_user(invalid_user))

    print(validate_user(missing_user))
    print(is_valid_user(missing_user))

if __name__ == '__main__':
    main()