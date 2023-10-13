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

# def prime_numbers(N):
#     prime_list = [2]

#     for number in range(3, N+1):
#         if not has_factors(number):
#             prime_list.append(number)
#     return prime_list

# def has_factors(number):

#     check_upto = ( number // 2) + 1

#     for item in range(2, check_upto):
#         if number % item == 0:
#             return True
#     return False

# print(prime_numbers(100))


# -----------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# def reverse_words_in(given_string):
#     word_present_index, space_checker, word_ending_index = 0, 0, len(given_string)-1
#     reversed_words = []

#     for space in given_string:
#         if space_checker < word_ending_index:
            
#             if space == ' ':
#                 reversed_words.insert(0, given_string[word_present_index:space_checker])
#                 space_checker += 1
#                 word_present_index = space_checker
#             elif space != ' ':
#                 space_checker += 1
#         else:
#             reversed_words.insert(0, given_string[word_present_index:word_ending_index + 1])
    
#     return ' '.join(reversed_words)

# print(reverse_words_in('Alice likes Bob'))


# -----------------------------------------------------------------------------
# --------------------------------------------------------------------------------



# replace d,d by a and remove b

def replace_d_d_by_a_and_remove_b(array_item):

    value = 0

    for item in range(len(array_item)):
        if array_item[value] == 'b':
            array_item.pop(value)
            value -= 1

        elif array_item[value] == 'a':
            array_item.pop(value)
            array_item.insert(value, 'd')
            array_item.insert(value, 'd')
            value += 1
            
        value += 1
            
    return array_item


print(replace_d_d_by_a_and_remove_b(["a", 'b', 'a', 'c']))

# input 1 :  [a, c, b, d, c, a ]
# oputop 1 : d d c d c d d

# input 2 : ["a", 'b', 'a', 'c']
# output 2 : ['d', 'd', 'd', 'd', 'c']






