# # Задача 1. Ввод данных и форматированный вывод
# X = int(input())
# Y = str(input())

# print(f'Меня зовут {Y}, мне {X} лет') 


# # задача 2. Сумма всех четных чиссел 
# cnt = int(input('Введи кол-во чисел: '))
# x=0
# numbers = []
# if cnt > 0:
#     for i in range(cnt):
#         number = int(input(f'Введи число {i+1}:'))
#         numbers.append(number)
#     for i in numbers:
#         if i%2==0:
#             x+=i
#     print(x)
# else:
#     print('Incorrect input!!!')


# # Задача 3: функция 
# def is_adult(age: int) -> bool:
#     return age>=18

# age = int(input('Enter your age: '))
# print(is_adult(age))



# Задача 4: func 2
def count_words(text: str) -> int:
    return len(text.split())
text=  'Иногда кажется, что время растягивается до бесконечности, когда мы ждем чего-то важного. А иногда оно пролетает'
print(count_words(text))