#!/usr/bin/python3

import vector
from vector import Vector


e1 = Vector("Error Test")
v1 = Vector(5)
v2 = Vector((10, 16))
v3 = Vector(range(2, 7))
v4 = Vector([1.3, 4.8, 9.1])
v5 = Vector([1, 4, 9])
v = [v1, v2, v3, v4, v5]
for i in v:
    print(i.values)
print(f"Vector sum with vector: {v4 + v5}\n")
print(f"Vector sum with scalar: {v4 + 2}\n")
print(f"Vector sub with vector: {v4 - v5}\n")
print(f"Vector sub with scalar: {v4 - 35}\n")
print(f"Vector product with vector: {v4 * v5}\n")
print(f"Vector product with scalar: {v4 * 10}\n")
print(f"Vector product with string: {v4 * 'teste'}\n")
print(f"Vector division by scalar: {v4 / 3}\n")
print(f"Vector division by vector: {v4 / v5}\n")
print(f"Vector rdivision by scalar: {1 / v5}\n")
print(f"String method: v4 = {str(v4)}")
print(f"Repr method: v4 = {repr(v4)}")
