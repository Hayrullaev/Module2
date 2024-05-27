
def find_unique_pairs(number):
    pairs = {}
    result = []
    for i in range(1, number):
        for j in range(i + 1, number + 1):
            pair = (i, j)
            if pair not in pairs and number % (i + j) == 0:
                pairs[pair] = True
                result.append(pair)
    return result

n = int(input("Введите число от 3 до 20: "))  # ввод числа
result = find_unique_pairs(n)  # вычисление пар
print("Пары чисел:", result)