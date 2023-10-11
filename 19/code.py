# Write a Python program that returns a string that is n (non-negative integer) copies of a given string.

def larger_string(text, n):
    result = ""
    for i in range(n):
        result = result + text
    return result


print(larger_string('abc', 2))
print(larger_string('.py', 3))
