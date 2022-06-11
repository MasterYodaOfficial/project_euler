from math import ceil, sqrt
from typing import Generator


def triangle_gen(start: int = 1) -> Generator:
    """Генератор треугольных чисел"""
    count_num: int = 2
    while True:
        yield start + count_num
        start = start + count_num
        count_num += 1


for triangle_num in triangle_gen():
    lens = 2
    half_num = ceil(sqrt(triangle_num))
    for i in range(2, half_num):
        if triangle_num % i == 0:
            lens += 2
    if half_num * 2 == triangle_num:
        lens -= 1
    if lens >= 500:
        print(f'Answer: {triangle_num}')
        break


