from typing import List, Set


def find_easy_nums(count_nums=10) -> int:
    """Находит простое число находящееся в заданном порядке"""
    easy_nums: List = [2, 3, 5, 7, 11, 13]
    not_easy_nums: Set = set(num ** 2 for num in easy_nums)
    current_num: int = 17
    while len(easy_nums) < count_nums:
        for num in easy_nums:
            if current_num in not_easy_nums:
                not_easy_nums.add(current_num ** 2)
                not_easy_nums |= set(current_num * num for num in easy_nums[:7])
                current_num += 2
                break
            if current_num ** 0.5 % 1 == 0:
                not_easy_nums.add(current_num ** 2)
                not_easy_nums |= set(current_num * num for num in easy_nums[:7])
                current_num += 2
                break
            if current_num % num == 0:
                not_easy_nums.add(current_num ** 2)
                not_easy_nums |= set(current_num * num for num in easy_nums[:7])
                current_num += 2
                break
        else:
            easy_nums.append(current_num)
            current_num += 2
    return easy_nums[-1]


answer = find_easy_nums(10001)
print(answer)
