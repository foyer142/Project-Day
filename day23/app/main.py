from cli import input_user_data, print_menu, print_user, print_users,print_error_validation
from storage import load_users, save_users
from services import UserService
from validators import UserValidator
from pathlib import Path
from custom_types import RawUserDict, UserDict


BASE_DIR = Path(__file__).resolve().parent.parent
FILENAME = BASE_DIR / "data" / "users.json"

def build_user(data: RawUserDict) -> UserDict:
    return {
        "name": data["name"],
        "age": int(data["age"]),
        "city": data["city"],
        "email": data["email"],
    }


def main() -> None:
    users = load_users(FILENAME)
    service = UserService(users)
    

    while True:
        print_menu()
        choice = input("Choose action: ")

        if choice == "1":
            data = input_user_data()
            validator = UserValidator(data)


            if validator.validate_user_data():
                user = build_user(data)

                service.add_user(user)
                save_users(FILENAME, service.get_all_users())
                print("User added and saved")
            else:
                print_error_validation(validator.errors)

        elif choice == "2":
            print_users(service.get_all_users())

        elif choice == "3":
            city = input("City: ")
            print_users(service.find_by_city(city))

        elif choice == "4":
            email = input("Email: ")
            print_user(service.find_by_email(email))

        elif choice == "5":
            save_users(FILENAME, service.get_all_users())
            print("Users saved")

        elif choice == "6":
            email = input("Email: ")

            if service.delete_by_email(email):
                save_users(FILENAME, service.get_all_users())
                print('User deleted')
            else:
                print('User not found')

        elif choice == "0":
            save_users(FILENAME, service.get_all_users())
            print("Goodbye")
            break

        else:
            print("Unknown action")


if __name__ == "__main__":
    main()
