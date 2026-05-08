
from user_service import UserService
from cli import print_menu, input_user_data, print_users, print_user


def main() -> None:
    service = UserService()

    while True:
        print_menu()
        choice = input("Choose action: ")

        if choice == "1":
            data = input_user_data()
            service.add_user(
                data["name"],
                data["age"],
                data["city"],
                data["email"],
            )
            print("User added")

        elif choice == "2":
            users = service.get_all_users()
            print_users(users)

        elif choice == "3":
            city = input("City: ")
            users = service.find_by_city(city)
            print_users(users)

        elif choice == "4":
            email = input("Email: ")
            user = service.find_by_email(email)
            print_user(user)

        elif choice == "0":
            print("Goodbye")
            break

        else:
            print("Unknown action")


if __name__ == "__main__":
    main()
