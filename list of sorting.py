def sort_by_length(lst):
    return sorted(lst, key=len)
# Test the function
my_list = ["apple", "banana", "cat", "dog", "elephant"]
print(sort_by_length(my_list))