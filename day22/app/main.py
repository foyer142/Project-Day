from cli import input_user_data, print_menu, print_user, print_users,print_error_validation
from storage import load_users, save_users
from service import UserService
from validator import UserValidator
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
FILENAME = BASE_DIR / "data" / "users.json"



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
                service.add_user(
                    data["name"],
                    data["age"],
                    data["city"],
                    data["email"],
                )
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
