import random

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[random.randint(1, 100) for i in range(cols)] for j in range(rows)]
        
    
    def check_sizes(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Size of matrices are different")
    
    def __str__(self):
        string = ""
        for row in range(self.rows):
            for col in range(self.cols):
                string += str(self.matrix[row][col]) + " "
            string += "\n"
        return string

    def __add__(self, other):
        self.check_sizes(other)
            
        result = Matrix(self.rows, self.cols)
        for row in range(self.rows):
            for col in range(self.cols):
                result.matrix[row][col] = self.matrix[row][col] + other.matrix[row][col]
        return result

    def __sub__(self, other):
        self.check_sizes(other)

        result = Matrix(self.rows, self.cols)
        for row in range(self.rows):
            for col in range(self.cols):
                result.matrix[row][col] = self.matrix[row][col] - other.matrix[row][col]
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Number of columns in the first matrix is not equal to the number of rows in the second matrix")

        result = Matrix(self.rows, other.cols)
        for row in range(self.rows):
            for col in range(other.cols):
                for i in range(self.cols):
                    result.matrix[row][col] += self.matrix[row][i] * other.matrix[i][col]
        return result


m1 = Matrix(2,3)
print("First matrix")
print(m1)

m2 = Matrix(2,3)
print("Second matrix")
print(m2)

print("Add")
print(m1 + m2)

print("Sub")
print(m1 - m2)

m1_for_mul = Matrix(2,3)
m2_for_mul = Matrix(3,2)

print("Mul")
print(m2_for_mul * m1_for_mul)
