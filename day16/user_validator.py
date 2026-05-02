import day16

def validate_users(users: list[dict]) -> list[dict]:
    validate_users_list = []
    for user in users:
        errors = day16.validate_user(user)
        user_dict = {
            'user' : user,
            'is_valid' : errors == [],
            'errors' : errors
        }
        validate_users_list.append(user_dict)
    return validate_users_list

def get_valid_users(users: list[dict]) -> list[dict]:
    return  [user for user in users if day16.is_valid_user(user)]

def main():
    
    users = [
        {
            "name": "Bulat",
            "age": 20,
            "email": "bulat@mail.com",
        },
        {
            "name": "Anna",
            "age": 17,
            "email": "anna@example.com",
        },
        {
            "name": "   ",
            "age": 25,
            "email": "emptyname@mail.com",
        },
        {
            "name": "Ivan",
            "age": "twenty",
            "email": "ivan@mail.com",
        },
        {
            "name": "Maria",
            "age": -5,
            "email": "maria@mail.com",
        },
        {
            "name": "Alex",
            "age": 130,
            "email": "alex@mail.com",
        },
        {
            "name": "NoEmail",
            "age": 30,
        },
        {
            "age": 22,
            "email": "noname@mail.com",
        },
        {
            "name": "BadEmail",
            "age": 21,
            "email": "bad-email",
        },
        {
            "name": "Good User",
            "age": 45,
            "email": "good.user@example.com",
        },
    ]
    reports = validate_users(users)

    print(reports)
    print(get_valid_users(users))



if __name__ == '__main__':
    main()