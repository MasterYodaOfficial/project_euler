from typing import List


def find_sum_nums(limit_num: int = 2000000) -> int:
    """Находит сумму простых чисел не больше лимита"""
    easy_nums: List = [num for num in range(limit_num)]
    easy_nums[1]: int = 0
    col: int = 2
    while col <= limit_num / 2 + 1:
        if easy_nums[col] != 0:
            ex_num = col * 2
            while ex_num < limit_num:
                easy_nums[ex_num] = 0
                ex_num += col
        col += 1
    return sum(easy_nums)


answer = find_sum_nums()
print(f'Ответ: {answer}')
