from typing import List


def find_easy_nums(count_nums=10) -> int:
    """Находит простое число находящееся в заданном порядке"""
    easy_nums: List = [2, 3, 5, 7, 11, 13]
    current_num: int = 17
    while len(easy_nums) < count_nums:
        for num in easy_nums:
            if current_num % num == 0:
                current_num += 2
                break
        else:
            easy_nums.append(current_num)
            current_num += 2
    return easy_nums[-1]


answer = find_easy_nums(10001)
print(f'Ответ: {answer}')
