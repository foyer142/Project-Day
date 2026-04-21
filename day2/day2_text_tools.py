
def count_words(text: str) -> int:
    return len(text.split())

def count_symbols(text: str) -> int:
    return len(text.replace(' ',''))

def upper_registr(text: str) -> str:
    return text.upper()

text = "Это просто пример строки с любым текстом"

print(count_words(text))
print(count_symbols(text))
print(upper_registr(text))
