# CLI user_manager

## What does program?
This is program can add info about user, save her, find user by email or city. Info saved in JSON file and before reboot program, info will remain into file. Программа работает как пользовательский менеджер. Он может сохранять новых пользователей, которых добавят и они не пропадут после закрытия программы. программа  ищет по почта, городу пользователей. программа может удалять пользователей.

## How to launch program?
You need change directory on "day22" and launch python file this command: 'python3 app/main.py'

## Which commands in menu program
1. add user
2. show user
3. find user by city
4. find user by email
5. save users
6. delete user by email
0. exit from program

## Structure files
day22/
    app/
        main.py
        cli.py
        storage.py
        validator.py
        service.py
    data/
        users.json

## What i learned
I learned: joining some files in one, do check conditions
 through try except, OOP.
Я выучил многое в этом проекте.
ООП, делать чтобы не зависило от определенной папки, разделять на функции, файлы и папки.
делать валидаторы.


