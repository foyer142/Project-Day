from custom_types import UserDict,RawUserDict,ValidationError

def print_menu() -> None:
    line = '1. Add user \n2. Show all users \n3. Find users by city \n4. Find user by email \n5. Save users \n6. Delete user by email \n0. Exit'
    print(line)


def input_user_data() -> RawUserDict:
    return {
        'name' : input("Name: ").strip(),
        'age' : input("Age: ").strip(),
        'city' : input("City: ").strip(),
        'email' : input("Email: ").strip()
    }



def print_users(users: list[UserDict]) -> None:
    if users == []:
        print('No users found')
    else:
        for user in users:
            print(', '.join(str(value) for value in user.values()))


def print_user(user: UserDict | None) -> None:
    if user is None:
        print("User not found")
    else:
        print(', '.join(str(value) for value in user.values()))

def print_error_validation(errors : list[ValidationError]) -> None:
    if not len(errors) == 0:
        for error in errors:
            print(error)
    else:
        print('Ошибок ввода нет.')