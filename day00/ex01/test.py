#!/usr/bin/python3

from matrix import InputError
from matrix import Matrix
from vector import Vector

a = Matrix([[2, 3], [9, 2]])
b = Matrix([[3, 1], [2, 8]])
v = Vector([1, 2])

print(f"a = \n{a}\n")
print(f"b = \n{b}\n")
print(f"v = \n{v}\n")
print(f"a + b = \n{a + b}\n")
print(f"a - b = \n{a - b}\n")
print(f"a * b = \n{a * b}\n")
print(f"a * v = \n{a * v}\n")
print(f"a * 10 = \n{a * 10}\n")
print(f"a / 8 = \n{a / 8}\n")
try:
    print(f"a / b = \n{a / b}\n")
except InputError as e:
    print(e.message)
