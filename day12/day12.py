import user_service

def main() -> None:

    users = [
    {"name": "  bulat  ", "age": 20, "city": "Tomsk"},
    {"name": "anna", "age": 17, "city": "Moscow"},
    {"name": "ivan", "age": 22, "city": "Tomsk"},
    ]

    users = user_service.normalize_users(users)

    for user in users:
        print(user_service.format_user(user))
    
    print('-----')
    for user in user_service.get_adult_users(users):
        print(user)
    

if __name__=='__main__':
    main()
