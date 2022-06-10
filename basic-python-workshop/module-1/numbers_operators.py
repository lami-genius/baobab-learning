# Operators, strongest at the bottom, weakest at the top
"""
or
and
not
in, not in, is, is not, <, <=, >, >=, !=, ==
|
^
&
<<, >>
+, -
*, /, //, %
+x, -x, ~x
**
"""
print("Power operator:  **")
print("2**4 = ", 2 ** 4)
print("-3**2 = ", -(3 ** 2))  # Evaluated as -3(3**2)
print("3**-2 = ", 3 ** -2)  # Evaluated as 1 / (3**2)
print("-" * 75)

print("Unary and bitwise operators: - ~")
# Logical negation
print("-4 = ", -4)
# Bitwise negation
# 2's compliment ~x = (-x) - 1
print("~4 = ", ~4, "(bitwise inversion, answer = -5)")
print("-" * 75)

print("Binary operators: + - * / % //")
print("The Floor operator // yields the quotient: 13.5//2 = ", 13.5 // 2)
print("The modulor operator % yields the remainder: 13.5%2 = ", 13.5 % 2)
print("-" * 75)

print("Shifting operators: >> <<")
print("100 >> 3 = ", 100 >> 3)
# 100 = 1100100 in binary
# Removing last 3 bits due to >> operation
# We obtain 1100 which yields 8+4=12
print(" " * 6, "same as: 100 // (2**3) = ", 100 // (2 ** 3))
print("100 << 3 = ", 100 << 3)
# 100 = 1100100 in binary
# Adding  3 0 bits at the end due to << operation
# We obtain 1100100000 which yields 512+256+32=800
print(" " * 6, "same as: 100 * (2**3) = ", 100 * (2 ** 3))
print("-" * 75)

print("Binary bitwise operators: | & ^")
print("Bitwise OR (pipe): 3 | 0 = ", 3 | 0)
print("Bitwise XOR (caret): 3 ^ 3 = ", 3 ^ 3)
print("Bitwise AND (ampersand): 3 & 0 = ", 3 & 0)
print("-" * 75)

print("Comparisons: >  >=  <  <=  ==  in  not in")
print("5 > 2?", 5 > 2)
print("5 == 3?", 5 == 3)
print("5 <= 4?", 5 <= 4)
print("2 in (1, 2, 3)?", 2 in (1, 2, 3))
print("5 not in (1, 2, 3)?", 5 not in (1, 2, 3))
print("-" * 75)

print("Boolean operators: AND OR NOT")
print("5 > 2 AND 5 == 2?", (5 > 2) and (5 == 2))
print("5 > 2 OR 5 == 2?", (5 > 2) or (5 == 2))
print("NOT (5 == 2 ", not (5 == 2))
print("-" * 75)

print("Multiple assignment")
a, b = 0, 1
print(a, b)
a, b = b, a
print(a, b)
a, b = 3 * a, 7 * b + 9 * a
print(a, b)
print("-" * 75)

# Use of math library
import math

var1, var2 = 2, 3
print("var1 = ", var1, ", var2 = ", var2)
print("round(var1 / var2) = ", round(var1 / var2))
print("math.ceil(var1 / var2) = ", math.ceil(var1 / var2))
print("math.floor(var1 / var2) = ", math.floor(var1 / var2))

print("pow(var1, var2) = ", pow(var1, var2))
print("math.pow(var1, var2) = ", math.pow(var1, var2))

print("abs(var1 - var2) = ", abs(var1 - var2))
print("math.sqrt(var2) = ", math.sqrt(var2))
print("-" * 75)
