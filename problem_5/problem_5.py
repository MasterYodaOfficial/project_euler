def check_divs(max_num, max_div=10):
    """Проверка числа на все делители"""
    for num in range(max_div, 1, -1):
        if max_num % num != 0:
            return False
    return True


def find_num(max_div: int) -> int:
    """Подбор числа для всех делителей."""
    current_num = max_div
    while True:
        if check_divs(current_num, max_div=max_div):
            return current_num
        current_num += max_div


answer = find_num(20)
print(f'Ответ: {answer}')
