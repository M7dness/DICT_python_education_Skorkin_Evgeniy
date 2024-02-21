# Функция для ввода матрицы с клавиатуры
def input_matrix(rows, cols):
    print(f"Enter {rows}x{cols} matrix:")
    matrix = []
    for _ in range(rows):
        matrix.append([float(x) for x in input().split()])
    return matrix


# Сложение матриц
def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])

    if len(matrix2) != rows or len(matrix2[0]) != cols:
        return None

    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result


# Умножение матрицы на число
def multiply_by_number(matrix, number):
    rows = len(matrix)
    cols = len(matrix[0])

    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix[i][j] * number)
        result.append(row)

    return result


# Умножение матриц
def multiply_matrices(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])

    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    if cols1 != rows2:
        return None

    result = []
    for i in range(rows1):
        row = []
        for j in range(cols2):
            cell = 0
            for k in range(cols1):
                cell += matrix1[i][k] * matrix2[k][j]
            row.append(cell)
        result.append(row)

    return result


# Транспонирование матрицы
def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = []
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        result.append(row)

    return result


# Вычисление определителя матрицы
def determinant(matrix):
    n = len(matrix)
    det = 0
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    for j in range(n):
        m = []
        for i in range(1, n):
            row = []
            for k in range(n):
                if k != j:
                    row.append(matrix[i][k])
            m.append(row)
        sign = (-1) ** j
        det += sign * matrix[0][j] * determinant(m)
    return det


# Нахождение обратной матрицы
def inverse(matrix):
    n = len(matrix)
    det = determinant(matrix)
    if det == 0:
        return None

    inverse = []
    for j in range(n):
        row = []
        for i in range(n):
            minor = []
            for k in range(n):
                if k != j:
                    minor.append(matrix[k][:i] + matrix[k][i + 1:])
            row.append(((-1) ** (i + j)) * determinant(minor))
        inverse.append(row)

    for i in range(n):
        for j in range(n):
            inverse[i][j] /= det

    return inverse


# Вывод матрицы
def print_matrix(matrix):
    for row in matrix:
        print(*[round(x, 2) for x in row])


# Основная программа
while True:
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")

    choice = int(input("Your choice: "))

    if choice == 1:
        a_rows, a_cols = [int(x) for x in input("Enter size of first matrix: ").split()]
        a = input_matrix(a_rows, a_cols)
        b_rows, b_cols = [int(x) for x in input("Enter size of second matrix: ").split()]
        b = input_matrix(b_rows, b_cols)
        c = add_matrices(a, b)
        if c is None:
            print("The operation cannot be performed.")
        else:
            print("The result is:")
            print_matrix(c)

    elif choice == 2:
        rows, cols = [int(x) for x in input("Enter size of matrix: ").split()]
        a = input_matrix(rows, cols)
        k = float(input("Enter constant: "))
        b = multiply_by_number(a, k)
        print("The result is:")
        print_matrix(b)

    elif choice == 3:
        a_rows, a_cols = [int(x) for x in input("Enter size of first matrix: ").split()]
        a = input_matrix(a_rows, a_cols)
        b_rows, b_cols = [int(x) for x in input("Enter size of second matrix: ").split()]
        b = input_matrix(b_rows, b_cols)
        c = multiply_matrices(a, b)
        if c is None:
            print("The operation cannot be performed.")
        else:
            print("The result is:")
            print_matrix(c)

    elif choice == 4:
        rows, cols = [int(x) for x in input("Enter size of matrix: ").split()]
        a = input_matrix(rows, cols)
        print("1. Main diagonal")
        print("2. Side diagonal")
        print("3. Vertical line")
        print("4. Horizontal line")
        choice = int(input("Your choice: "))
        b = transpose(a)
        print("The result is:")
        print_matrix(b)

    elif choice == 5:
        n = int(input("Enter size of matrix: "))
        a = input_matrix(n, n)
        det = determinant(a)
        print(f"The result is:\n{det}")

    elif choice == 6:
        n = int(input("Enter matrix size: "))
        matrix = input_matrix(n, n)
        inv = inverse(matrix)
        if inv is None:
            print("This matrix doesn't have an inverse.")
        else:
            print("The result is:")
            print_matrix(inv)

    elif choice == 0:
        break
