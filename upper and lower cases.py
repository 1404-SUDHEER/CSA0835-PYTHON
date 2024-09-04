def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

# Test the function
my_string = "Hello, World!"
upper, lower = count_case(my_string)
print(f"Upper case letters: {upper}")
print(f"Lower case letters: {lower}")