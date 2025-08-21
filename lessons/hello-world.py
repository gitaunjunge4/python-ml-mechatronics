# Day 1 

print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(3 % 2)             # modulus(%)
print(3 // 2)            # Floor division operator(//)

# Checking data types
print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Gitau'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Gitau'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple

# Find an Euclidian distance between (2, 3) and (10, 8)
def pyTheorem(a, b):
    result = (a**2 + b**2)**0.5
    return result
print(pyTheorem(2,3))
print(pyTheorem(10,8))