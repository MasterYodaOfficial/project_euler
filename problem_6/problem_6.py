def difference_sums(count_nums=10):
    return sum(num2 for num2 in range(1, count_nums + 1)) ** 2 - sum(num ** 2 for num in range(1, count_nums + 1))


answer = difference_sums(100)
print(f'Ответ: {answer}')
