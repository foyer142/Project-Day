# CLI user_manager

## What does program?
 Программа работает как пользовательский менеджер. Он может сохранять новых пользователей, которых добавят и они не пропадут после закрытия программы. Программа  ищет по почте, городу пользователей. Программа может удалять пользователей после ввода почта по почте. Есть проверка валидности данных при добавлении нового пользователя: проверка на пустую строку, проверка возраста (он должен быть числом и от 0 до 120 лет), проверка валидности почты на содержание символов "@" и ".", а также их последовательностей. 

## How to launch program?
Нужно перейти в папку где находится сама программа и запустить через CLI командой: 'python3 app/main.py'

## Which commands in menu program
1. add user
2. show user
3. find user by city
4. find user by email
5. save users
6. delete user by email
0. exit from program

## Structure files
../
    app/
        __init__.py
        main.py
        cli.py
        storage.py
        validators.py
        services.py
        custom_types.py
    data/
        users.json
    README.md

## What i learned
В этом проекте было изучено многое, главное из этого это: ООП, типизация, работа с JSON файлом, стркутура самого проекта (разбиение на папки, подфайлы, импортирование файлов)

## Example valid input
name - Myke
age - 42
city - Budapesht
email - kpss@dayson.no

## Example invalid input
1.
    name - Myke
    age - abf
    city - Budapesht
    email - kpss@dayson.no
2.
    name - Myke
    age - 42
    city - Budapesht
    email - kpssdayson.no
3.
    name - 
    age - 42
    city - Budapesht
    email - kpss@dayson.

## Data flow
raw input -> validation -> typed user -> service -> storage
идет ввод данных пользователя (они сырые, то есть все данные в типе строки)
дальше идет валидация данных, могут ли данные быть преобразованы, записаны, типизированы
дальше идет типизация и преобразование данных 
данные пользователя попадают в список пользователя
дальше саписок пользователей попадает в хранилище JSON

