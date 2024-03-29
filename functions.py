#TODO: Make custom exceptions
#TODO: You shouldn't be able to delete a single element from a row, only full rows and columns

from random import randint
from copy import deepcopy


class Matrix(object):

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = []

        for i in range(rows):
            self.matrix.append([]) # Initialize empty rows

        for row in self.matrix:
            for i in range(columns):
                row.append(0) # Fill the rows with 0s

    def __repr__(self):
        """Print the matrix row after row."""
        rep = ""
        for row in self.matrix:
            rep += str(row)
            rep += "\n"
        return rep.rstrip()

    def __getitem__(self, key):
        return self.matrix[key]

    def __setitem__(self, key, value):
        if isinstance(value, list):
            self.matrix[key] = value
        else:
            raise TypeError("A matrix object can only contain lists of numbers")
        return

    def __delitem__(self, key):
        del(self.matrix[key])
        self.rows = self.rows - 1
        return

    def __contains__(self, value):
        for row in self.matrix:
            for element in row:
                if element == value:
                    return True
                else:
                    pass
        return False

    def __eq__(self, otherMatrix):
        if isinstance(otherMatrix, Matrix):
            if (self.rows != otherMatrix.rows) or (self.columns != otherMatrix.columns):
                return False # They don't have the same dimensions, they can't be equal

            for row in range(self.rows): # Check the elements one by one
                for column in range(self.columns):
                    if self.matrix[row][column] != otherMatrix[row][column]:
                        return False

            return True
        else:
            return False

    def __ne__(self, otherMatrix):
        return not self.__eq__(otherMatrix) # Check for equality and reverse the result

    def __add__(self, otherMatrix):
        '''Add 2 matrices of the same type.'''
        return self.__add_or_sub(otherMatrix, "add")

    def __sub__(self, otherMatrix):
        '''Subtracts otherMatrix from self.'''
        return self.__add_or_sub(otherMatrix, "sub")

    def __mul__(self, secondTerm):
        if isinstance(secondTerm, (int, float, complex)):
            return self.__scalar_product(secondTerm)
        elif isinstance(secondTerm, Matrix):
            if self.columns == secondTerm.rows:
                newMatrix = Matrix(self.rows, secondTerm.columns)
                transposeMatrix = secondTerm.transpose()
                '''
                Matrix multiplication is done iterating through each column of the
                second term. We calculate the transpose of the second matrix because
                it gives us a list for each column, which is far easier to iterate
                through.
                '''

                for row_self in range(self.rows):
                    for row_transpose in range(transposeMatrix.rows):
                        '''
                        The rows of the transpose correspond to the columns
                        of the original matrix.
                        '''
                        new_element = 0
                        for column_self in range(self.columns):
                            new_element += (self[row_self][column_self] * transposeMatrix[row_transpose][column_self])

                        newMatrix[row_self][row_transpose] = new_element

                return newMatrix

            else:
                raise Exception(
                    "Can't multiply (%d, %d) matrix with (%d, %d) matrix" %
                    (self.rows, self.columns, secondTerm.rows, secondTerm.columns)
                )
        else:
            raise TypeError("Can't multiply a matrix by non-int of type " + type(secondTerm).__name__)

    def __rmul__(self, secondTerm):
        return self.__mul__(secondTerm)

    def __scalar_product(self, number):
        newMatrix = Matrix(self.rows, self.columns)

        for row in range(self.rows):
            for column in range(self.columns):
                newMatrix[row][column] = self[row][column] * number

        return newMatrix

    def __add_or_sub(self, secondTerm, operation):
        newMatrix = Matrix(self.rows, self.columns)

        if isinstance(secondTerm, (int, float, complex)):
            for row in range(self.rows):
                for column in range(self.columns):
                    if operation == "add":
                        newMatrix[row][column] = self[row][column] + secondTerm
                    if operation == "sub":
                        newMatrix[row][column] = self[row][column] - secondTerm
        elif isinstance(secondTerm, Matrix):
            if (self.rows == secondTerm.rows) and (self.columns == secondTerm.columns):
                for row in range(self.rows):
                    for column in range(self.columns):
                        if operation == "add":
                            newMatrix[row][column] = self[row][column] + secondTerm[row][column]
                        elif operation == "sub":
                            newMatrix[row][column] = self[row][column] - secondTerm[row][column]
                        else:
                            raise Exception("Invalid operation type")
            else:
                raise TypeError(
                    "Can't add or subtract (%d, %d) matrix with (%d, %d) matrix" %
                    (self.rows, self.columns, secondTerm.rows, secondTerm.columns)
                )
        else:
            raise TypeError("Can only add or subtract a matrix with another matrix or a number")

        return newMatrix

    def is_square(self):
        return self.rows == self.columns

    def transpose(self):
        newMatrix = Matrix(self.columns, self.rows)

        for row in range(self.rows):
            for column in range(self.columns):
                newMatrix[column][row] = self.matrix[row][column] # a(i,j) = a(j,i)

        return newMatrix

    def complement_matrix(self, rowToDelete, columnToDelete):
        newMatrix = deepcopy(self)
        del(newMatrix[rowToDelete])

        for row in range(newMatrix.rows):
            del(newMatrix[row][columnToDelete])

        newMatrix.columns -= 1

        return newMatrix

    def algebric_complement(self, row, column):
        complementMatrix = self.complement_matrix(row, column)
        algebricComplement = (-1)**(row+column) * complementMatrix.determinant()

        return algebricComplement

    def determinant(self):
        '''
        Return the determinant.

        This function uses Laplace's theorem to calculate the determinant.
        It is a very rough implementation, which means it becomes slower and
        slower as the size of the matrix grows.
        '''
        if self.is_square():
            if self.rows == 1:
                # If it's a square matrix with only 1 row, it has only 1 element
                det = self[0][0] # The determinant is equal to the element
            elif self.rows == 2:
                det = (self[0][0] * self[1][1]) - (self[0][1] * self[1][0])
            else:
                # We calculate the determinant using Laplace's theorem
                det = 0
                for element in range(self.columns):
                    det += self[0][element] * self.algebric_complement(0, element)
            return det
        else:
            raise TypeError("Can only calculate the determinant of a square matrix")

    def algebric_complements_matrix(self):
        '''Return the matrix of all algebric complements.'''
        if self.is_square():
            newMatrix = Matrix(self.rows, self.columns)
            for row in range(self.rows):
                for column in range(self.columns):
                    newMatrix[row][column] = self.algebric_complement(row, column)
            return newMatrix
        else:
            raise TypeError("Algebric complements can only be calculated on a square matrix")

    def inverse_matrix(self):
        '''Return the inverse matrix.'''
        det = self.determinant()
        if det == 0:
            raise Exception("Matrix not invertible")
        else:
            algebricComplementsMatrix = self.algebric_complements_matrix()
            inverseMatrix = 1/det * algebricComplementsMatrix.transpose()

            return inverseMatrix

    def symmetric_part(self):
        '''Return the symmetric part of the matrix.'''
        newMatrix = 1/2 * (self + self.transpose())

        return newMatrix

    def antisymmetric_part(self):
        '''Return the antisymmetric part of the matrix.'''
        newMatrix = 1/2 * (self - self.transpose())

        return newMatrix

    def random(self, lower=-5, upper=5):
        '''Fill the matrix with random numbers (integers).'''
        for row in self.matrix:
            for i in range(self.columns):
                row[i] = randint(lower, upper)


def solve(equations):
    # the constants of a system of linear equations are stored in a list for each equation in the system
    """
    for example the system below:
         2x+9y-3z+7w+8=0
         7x-2y+6z-1w-10=0
         -8x-3y+2z+5w+4=0
         0x+2y+z+w+0=0
    is expressed as the list:
         [[2,9,-3,7,8],[7,-2,6,-1,-10],[-8,-3,2,5,4],[0,2,1,1,0]]
    """
    lists = []  # I failed to name it meaningfully
    for eq in range(len(equations)):
        # print "equations 1", equations
        # find an equation whose first element is not zero and call it index
        index = 0
        for i in range(len(equations)):
            if equations[i][0] != 0:
                index = i;
                break;
        # print "index "+str(eq)+": ",index
        # for the equation[index] calc the lists next itam  as follows
        lists.append([-1.0 * i / equations[index][0] for i in equations[index][1:]])
        # print "list"+str(eq)+": ", lists[-1]
        # remve equation[index] and modify the others
        equations.pop(index)
        for i in equations:
            for j in range(len(lists[-1])):
                i[j + 1] += i[0] * lists[-1][j]
            i.pop(0)
    lists.reverse()
    answers = [lists[0][0]]
    for i in range(1, len(lists)):
        tmpans = lists[i][-1]
        for j in range(len(lists[i]) - 1):
            tmpans += lists[i][j] * answers[-1 - j]
        answers.append(tmpans)
    answers.reverse()
    return answers