# -----------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# finding duplicate items in array

# def find_duplicate_item():
#     original_array = list(int,input().split(','))
#     duplicate_items = []

#     for duplicate in original_array:
#         if original_array.count(duplicate) > 1:
#             duplicate_items.append(duplicate)
            
#     return duplicate_items

# print(find_duplicate_item())

# -----------------------------------------------------------------------------
# --------------------------------------------------------------------------------



# prime number

def prime_numbers(N):
    prime_list = [2]

    for number in range(3, N+1):
        if not has_factors(number):
            prime_list.append(number)
    return prime_list

def has_factors(number):

    check_upto = ( number // 2) + 1

    for item in range(2, check_upto):
        if number % item == 0:
            return True
    return False

print(prime_numbers(100))






