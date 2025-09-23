# Екі өлшемді массив (мысал үшін 3x3)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Әр жолдың қосындысы
for i in range(len(matrix)):
    row_sum = sum(matrix[i])
    print(f"{i+1}-жолдың қосындысы:", row_sum)6.py