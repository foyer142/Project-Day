
def print_menu() -> None:
    line = '1. Add user \n2. Show all users \n3. Find users by city \n4. Find user by email \n5. Save users \n6. Delete user by email \n0. Exit'
    print(line)


def input_user_data() -> dict:
    not_done = True 
    while not_done:
        user_data = {}
        try:
            name = input('Name:')
            age = int(input('Age:'))
            city = input('City:')
            email = input('Email:')
            user_data = ({
                "name": name,
                "age": age,
                "city": city,
                "email": email,
            })
            if all(user_data.values()):
                not_done = False
            else:
                not_done = True
                print('Поля не должны быть пустыми...')
        except ValueError:
            print('Неправильный тип введенных данных... ')
        

    return ({
        "name": name,
        "age": age,
        "city": city,
        "email": email,
    })

def print_users(users: list[dict]) -> None:
    if users == []:
        print('No users found')
    else:
        for user in users:
            print(', '.join(str(value) for value in user.values()))


def print_user(user: dict | None) -> None:
    if user is None:
        print("User not found")
    else:
        print(', '.join(str(value) for value in user.values()))