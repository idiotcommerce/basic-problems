
# finding duplicate items in array

def find_duplicate_items():

    original_array = list(input().split(','))
    duplicate_items = []

    for duplicate in original_array:
        if original_array.count(duplicate) > 1:
            duplicate_items.append(duplicate)
            
    return duplicate_items

print(find_duplicate_items())
















