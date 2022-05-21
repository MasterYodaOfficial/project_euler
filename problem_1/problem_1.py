def sum_divs(max_num: int) -> int:
    """Возвращает сумму чисел кратных 3 и 5 не превышающих max_num"""
    return sum(num for num in range(1, max_num) if num % 3 == 0 or num % 5 == 0)


answer = sum_divs(1000)
print(f'Ответ: {answer}')
