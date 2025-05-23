import re

def linear_search(lst, pattern):
    # Compile the pattern using re
    regex = re.compile(pattern)
    
    for index, element in enumerate(lst):
        if regex.search(element):
            return f"Pattern found in element '{element}' at index {index}"
    
    return "Pattern not found in the list"

# Example list
my_list = ["apple", "banana", "cherry", "date", "elderberry"]
pattern = "an" 
result = linear_search(my_list, pattern)
print(result)