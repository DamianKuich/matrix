from functions import *
import numpy as np

q = False
choice = ''


def get_user_choice():
    return input()


def greeter():
    # Let users know what they can do.
    print("Welcome to my simple Matrix operations program wrote in python!\n")
    print("Write quit if you want exit the program\n")
    print("If you want to create one matrix size NxM with your input: matrix\n")
    print("If you want to create matrix size NxM with random numbers just write: random\n")
    print("If you want to create two matrices with size NxM write: two")


def function_choice_one():
    print("Write what you want to do:\n")
    print("1: inverse\n")
    print("2: transpose\n")
    print("3: determinant\n")
    print("4: multiply by scalar\n")
    print("5: rank\n")
    print("6: If you want to delete row by yourself\n")


def function_choice_two():
    print("Write what you want to do:\n")
    print("1: multiplication\n")
    print("2: addition\n")
    print("3: subtraction\n")
    print("4: Solve a linear matrix equation\n")


def function_subtraction_matrix():
    print("If you want to subtract one row from another write like this(for example the first to take away from the "
          "second): - 2 1")
    print("Write exit to close")


greeter()
while not q:
    choice = get_user_choice()
    if choice == 'quit':
        break
    elif choice == 'matrix':
        n, m = (input("Write size of your matrix for example: 3 3\n").split())
        n = int(n)
        m = int(m)
        matrix = Matrix(n, m)
        print("Input your data in new line\n")
        for i in range(n):
            for j in range(m):
                matrix[i][j] = int(input())
        print(matrix)
        function_choice_one()
        choice = get_user_choice()
        if choice == '1':
            print(matrix.inverse_matrix())
        elif choice == '2':
            print(matrix.transpose())
        elif choice == '3':
            print(matrix.determinant())
        elif choice == '4':
            scalar = int(input("Podaj scalar: "))
            print(matrix * scalar)
        elif choice == '5':
            print(np.linalg.matrix_rank(matrix))

    elif choice == 'random':
        n, m = (input("Write size of your matrix for example: 3 3\n").split())
        n = int(n)
        m = int(m)
        matrix = Matrix(n, m)
        matrix.random()
        print(matrix)
        function_choice_one()
        choice = get_user_choice()
        if choice == '1':
            print(matrix.inverse_matrix())
        elif choice == '2':
            print(matrix.transpose())
        elif choice == '3':
            print(matrix.determinant())
        elif choice == '4':
            scalar = int(input("Write scalar: "))
            print(matrix * scalar)
        elif choice == '5':
            print(np.linalg.matrix_rank(matrix))
        elif choice == '6':
            function_subtraction_matrix()
            counter = True
            while counter:
                b = [x for x in input().split()]
                if b == 'exit':
                    break
                else:
                    o1 = int(b[1])
                    o2 = int(b[2])
                    print(o1)
                    print(o2)
                    if b[0] == '-':
                        for i in range(m):
                            matrix[o1 - 1][i] = -1 * matrix[o2 - 1][i] + matrix[o1 - 1][i]
                        print(matrix)
                    elif b[0] == '+':
                        for i in range(n):
                            matrix[o1 - 1][i] = matrix[o2 - 1][i] + matrix[o1 - 1][i]
                        print(matrix)

    elif choice == 'two':
        function_choice_two()
        choice = get_user_choice()
        if choice == '4':
            a = np.array([[3, 1], [1, 2]])
            b = np.array([9, 8])
            print(np.linalg.solve(a, b))
            n, m = (input("Write size of your matrix for example: 3 3\n").split())
            n = int(n)
            m = int(m)
            matrix1 = []
            print("Input your data in new line\n")
            for i in range(n):
                row_list = []
                for j in range(m):
                    row_list.append(int(input()))  # add the input to row list
                matrix1.append(row_list)
            print("Input your vector with spaces\n")
            matrix2 = list(map(int, input().split()))
            for k in range(m):
                matrix1[k].append(matrix2[k])
            print(solve(matrix1))
        elif choice == '1':
            n, m = (input("Write size of your first matrix for example: 3 3\n").split())
            n = int(n)
            m = int(m)
            matrix1 = Matrix(n, m)
            print("Input your data in new line\n")
            for i in range(n):
                for j in range(m):
                    matrix1[i][j] = int(input())
            n, m = (input("Write size of your second matrix for example: 3 3\n").split())
            n = int(n)
            m = int(m)
            matrix2 = Matrix(n, m)
            print("Input your data in new line\n")
            for i in range(n):
                for j in range(m):
                    matrix2[i][j] = int(input())
            print(matrix1 * matrix2)

        elif choice == '2':
            n, m = (input("Write size of your first matrix for example: 3 3\n").split())
            n = int(n)
            m = int(m)
            matrix1 = Matrix(n, m)
            print("Input your data in new line\n")
            for i in range(n):
                for j in range(m):
                    matrix1[i][j] = int(input())
            n, m = (input("Write size of your second matrix for example: 3 3\n").split())
            n = int(n)
            m = int(m)
            matrix2 = Matrix(n, m)
            print("Input your data in new line\n")
            for i in range(n):
                for j in range(m):
                    matrix2[i][j] = int(input())
            print(matrix1 + matrix2)

        elif choice == '3':
            n, m = (input("Write size of your first matrix for example: 3 3\n").split())
            n = int(n)
            m = int(m)
            matrix1 = Matrix(n, m)
            print("Input your data in new line\n")
            for i in range(n):
                for j in range(m):
                    matrix1[i][j] = int(input())
            n, m = (input("Write size of your second matrix for example: 3 3\n").split())
            n = int(n)
            m = int(m)
            matrix2 = Matrix(n, m)
            print("Input your data in new line\n")
            for i in range(n):
                for j in range(m):
                    matrix2[i][j] = int(input())
            print(matrix1 - matrix2)
