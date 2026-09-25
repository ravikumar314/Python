# Arithmetic operator
a = 4
b = 4
c = 4
d = a - b + c

# sum
print(a + b + c)
print(c)


# Assignment operator
a = 4 - 2
b = 6
b += 3
print(b)


# Comparison operator
d = 5 > 4
print(d)


# Logical operator
e = True or False
print(e)

'''
the expression f = 10 and 5 assigns the value 5 to the variable f because the logical 
and operator evaluates from left to right and returns the first falsy value, or the
last value if all operands are truthy
'''
f = -1 and 10
print(f)
print(not(True))