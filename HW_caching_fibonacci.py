def caching_fibonacci():
    cache = {}  # Створюємо порожній словник для збереження обчислених значень

    def fibonacci(n):
        if n in cache:  # Якщо значення вже обчислено — повертаємо його з кешу
            return cache[n]
        if n == 0:  # Базовий випадок: fib(0) = 0
            result = 0
        elif n == 1:  # Базовий випадок: fib(1) = 1
            result = 1
        else:
            # Рекурсивний виклик з використанням кешу
            result = fibonacci(n - 1) + fibonacci(n - 2)
        cache[n] = result  # Зберігаємо результат у кеші
        return result

    return fibonacci  # Повертаємо внутрішню функцію fibonacci
