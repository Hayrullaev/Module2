def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        row = []
        matrix.append(row)
        for j in range(m):
            row.append(value)
    return matrix

result1 = get_matrix(5, 5,2)
result2 = get_matrix(3,9,24)
result3 = get_matrix(5, 6, 45)
print(result1)
print(result2)
print(result3)
