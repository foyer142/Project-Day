
def get_even_numbers(numbers: list[int]) -> list[int]:
    even_numbers = []
    for num in numbers:
        if num%2==0:
            even_numbers.append(num)
    return even_numbers

def get_positive_numbers(numbers: list[int]) -> list[int]:
    positive_numbers = []
    for number in numbers:
        if number > 0:
            positive_numbers.append(number)
    return positive_numbers

def find_max_number(numbers: list[int]) -> int:
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

def calculate_average(numbers: list[int]) -> float:
    return sum(numbers)/len(numbers)

numbers = [-7, -5, -3, -1, 0, 1, 2, 4, 6, 8, -10, 11, -12, 13, 15]
print(get_even_numbers(numbers))
print(get_positive_numbers(numbers))
print(find_max_number(numbers))
print(calculate_average(numbers))


