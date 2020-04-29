#!/usr/bin/python3
from vector import Vector


class InputError(Exception):
    def __init__(self, message="User input error."):
        self.message = message


class Matrix:

    def __init__(self, data, shape=None):
        if isinstance(data, list):
            if len(set([len(i) for i in data])) > 1:
                raise InputError("Unequal matrix dimensions.")
            self.data = data
        elif isinstance(data, tuple):
            if len(data) != 2:
                raise InputError("Invalid matrix shape.")
            self.data = [[0 for i in range(data[0])] for i in range(data[1])]
        else:
            raise InputError("Invalid matrix data.")

    @property
    def shape(self):
        return (len(self.data), len(self.data[0]))

    def __neg__(self):
        return self * -1

    def __add__(self, m2):
        m1 = self
        if not isinstance(m1, Matrix) or not isinstance(m2, Matrix):
            raise InputError("Invalid operands for matrix sum.")
        elif m1.shape != m2.shape:
            raise InputError("Cannot add matrices with different shapes.")
        else:
            result = []
            for k in range(m1.shape[1]):
                result.append([i + j for i, j in zip(m1.data[k], m2.data[k])])
            return Matrix(result)

    def __radd__(self, m2):
        return self + m2

    def __sub__(self, m2):
        return self + -m2

    def __rsub__(self, m2):
        return -self + m2

    def __mul__(self, m2):
        if isinstance(m2, (int, float)):
            result = []
            for k in range(self.shape[1]):
                result.append([i * m2 for i in self.data[k]])
            return Matrix(result)
        elif isinstance(m2, Vector):
            if self.shape[0] != m2.size:
                raise InputError("Cannot multiply matrix for n-sized vector.")
            result = []
            for k in range(self.shape[1]):
                result.append(Vector(self.data[k]) * m2)
            return result
        elif isinstance(m2, Matrix):
            if self.shape != m2.shape:
                raise InputError("Cannot multiply unequal shapes matrices.")
            result = []
            for k in range(self.shape[1]):
                row = []
                for l in range(self.shape[0]):
                    col = Vector([i[l] for i in m2.data])
                    row.append(Vector(self.data[k]) * col)
                result.append(row)
            return Matrix(result)
        else:
            raise InputError("Can't multiply matrix by this data type.")

    def __rmul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return self * scalar
        else:
            raise InputError("Can't multiply this type by matrix.")

    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)):
            return self * (scalar ** -1)
        else:
            raise InputError("Can't divide matrix by this type.")

    def __rtruediv__(self, scalar):
        raise InputError("Operation undefined.")

    def __str__(self):
        result = "["
        for i in range(self.shape[0]):
            result += str(self.data[i])
            if i != self.shape[0] - 1:
                result += '\n '
        result += "]"
        return (result)

    def __repr__(self):
        result = "Matrix(["
        for i in range(self.shape[0]):
            result += str(self.data[i])
            if i != self.shape[0] - 1:
                result += '\n        '
        result += "])"
        return (result)
