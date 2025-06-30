import re

# Функція-генератор, яка знаходить усі дійсні числа у тексті
def generator_numbers(text: str):
    # Патерн шукає дійсні числа з пробілами з обох боків, напр. ' 123.45 '
    pattern = r'\s\d+\.\d+\s'
    for match in re.findall(pattern, text):
        yield float(match)  # Повертаємо число у форматі float

# Функція для підрахунку загального доходу з тексту
def sum_profit(text: str, func):
    return sum(func(text))  # Підсумовуємо всі числа, знайдені генератором
