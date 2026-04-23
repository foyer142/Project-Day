# Задание 1 
def reverse_text(text: str) -> str:
    return text[::-1]

txt = 'В статистике коллекциями называют совокупности данных, состоящие из отдельных наблюдений, используемых для анализа.'
print('Задание 1',reverse_text(txt))

# Задание 2
def count_vowels(text: str) -> int:
    vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    cnt = 0
    for i in text.lower():
        if i in vowels:
            cnt+=1
    return cnt
txt = 'В статистике коллекциями называют совокупности данных, состоящие из отдельных наблюдений, используемых для анализа.'
print('Задание 2',count_vowels(txt))


# Задание 3
def find_longest_word(text: str) -> str:
    default = 0
    finaly_word = ''
    for i in text.split():
        if len(i) >= default:
            default = len(i)
            finaly_word = i
    return finaly_word

txt = 'В статистике коллекциями называют совокупности данных, состоящие из отдельных наблюдений, используемых для анализа.'
print('Задание 3',find_longest_word(txt))

# Задание 4
def unique_numbers(numbers: list[int]) -> list[int]:
    unique = []
    for i in numbers:
        if i not in unique:
            unique.append(i)    
    return unique

numbers = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 9, 10, 1, 11, 12]
print('Задание 4',unique_numbers(numbers))