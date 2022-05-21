from typing import List


def find_pali(count_digit=3) -> int:
    """Находит максимальный палиндром произведения трехзначных чисел"""
    all_palis: List = []
    for first_factor in range(int('9' * count_digit), int('9' * (count_digit - 1)), -1):
        for second_factor in range(int('9' * count_digit), int('9' * (count_digit - 1)), -1):
            current_num = str(first_factor * second_factor)
            if current_num == current_num[::-1]:
                all_palis.append(int(current_num))
    return max(all_palis)


answer = find_pali()
print(f'Ответ: {answer}')


