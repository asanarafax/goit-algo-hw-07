def caching_fibonacci():

    cache = {}

    def fibonacci(n):

        if n <= 0:
            return 0
        elif n == 1:
            return 1

        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

fib = caching_fibonacci()
print(fib(10))  # 55
print(fib(15))  # 610





import re
from typing import Callable

def generator_numbers(text: str):
    """
    Генератор, що знаходить усі дійсні числа у тексті
    та повертає їх одне за одним.
    """
    # регулярний вираз для пошуку чисел з десятковою крапкою
    pattern = r"\d+\.\d+|\d+"
    for match in re.findall(pattern, text):
        yield float(match)


def sum_profit(text: str, func: Callable):
    """
    Використовує generator_numbers для обчислення
    загальної суми чисел у тексті.
    """
    return sum(func(text))


# приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

















































