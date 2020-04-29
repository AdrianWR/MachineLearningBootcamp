#!/usr/bin/python3


class BaseError(Exception):
    def __init__(self, message):
        self.message = message
        pass


class InputError(BaseError):
    pass


class VectorSpaceError(BaseError):
    def __init__(self, expression, message):
        super().__init__(message)
        self.expression = expression


class Vector(object):
    def __init__(self, values):
        try:
            if isinstance(values, int):
                values = range(values)
            elif isinstance(values, tuple) and len(values):
                values = range(values[0], values[1])
            elif not (isinstance(values, range) or isinstance(values, list)):
                raise InputError("Argument type not accepted.")
            self.values = [float(i) for i in values]
        except InputError as e:
            print(e.message)
        pass

    @property
    def size(self):
        return len(self.values)

    def __add__(self, other):
        return self.__vector_sum(other)

    def __radd__(self, other):
        return self.__vector_sum(other)

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        return self.__vector_product(other)

    def __rmul__(self, other):
        return self.__vector_product(other)

    def __truediv__(self, other):
        try:
            if isinstance(other, (int, float)):
                other = float(other) ** -1
                result = self.__vector_product(other)
            else:
                raise(InputError("Cannot divide by non-scalar."))
        except InputError as e:
            print(e.message)
            pass
        else:
            return result

    def __rtruediv__(self, other):
        try:
            if isinstance(other, (int, float)):
                raise InputError("Cannot divide scalar by vector.")
            elif isinstance(other, Vector):
                raise InputError("Cannot divide vector by vector.")
            else:
                raise InputError("Operation undefined.")
        except InputError as e:
            print(e.message)

    def __str__(self):
        return str(self.values)

    def __repr__(self):
        return f"Vector({str(self)})"

    def __neg__(self):
        return Vector([-i for i in self.values])

    def __vector_sum(self, other):
        try:
            if isinstance(other, int) or isinstance(other, float):
                raise VectorSpaceError(None, "Cannot add scalar to vector.")
            elif not isinstance(other, Vector):
                raise InputError("Cannot add non-vector object.")
            elif self.size != other.size:
                exp = f"size  {self.size} != size {other.size}"
                raise VectorSpaceError(exp, "Cannot add vectors "
                                            "from distinct vector spaces.")
        except InputError as e:
            print(e.message)
            pass
        except VectorSpaceError as e:
            if (e.expression):
                print(e.expression)
            print(e.message)
            pass
        else:
            sum = [i + j for i, j in zip(self.values, other.values)]
            return Vector(sum)

    def __vector_product(self, other):
        try:
            if isinstance(other, Vector):
                if self.size != other.size:
                    exp = f"size  {self.size} != size {other.size}"
                    message = """Cannot multiply vectors
                                 from distinct vector spaces."""
                    raise VectorSpaceError(exp, message)
                else:
                    result = [i * j for i, j in zip(self.values, other.values)]
                    result = sum(result)
            elif isinstance(other, (int, float)):
                other = float(other)
                result = Vector([i * other for i in self.values])
            else:
                raise InputError("Cannot multiply non-vector object.")
        except InputError as e:
            print(e.message)
        except VectorSpaceError as e:
            if (e.expression):
                print(e.expression)
            print(e.message)
        else:
            return result
