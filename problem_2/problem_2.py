from typing import List


def sum_fib(max_num: int) -> int:
    """Возвращает сумму четных чисел Фибоначи не превышающих max_num"""
    all_fibs: List = [1, 2]
    current_num: int = 1
    next_num: int = 2
    while current_num < max_num:
        num_fib = current_num + next_num
        all_fibs.append(num_fib)
        current_num, next_num = next_num, num_fib
    return sum(num for num in all_fibs if num % 2 == 0)


answer = sum_fib(4000000)
print(f'Ответ: {answer}')
