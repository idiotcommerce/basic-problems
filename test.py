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

def reverse_words_in(given_string):
    word_present_index, space_checker, word_ending_index = 0, 0, len(given_string)-1
    reversed_words = []

    for space in given_string:
        if space_checker < word_ending_index:
            
            if space == ' ':
                reversed_words.insert(0, given_string[word_present_index:space_checker])
                space_checker += 1
                word_present_index = space_checker
            elif space != ' ':
                space_checker += 1
        else:
            reversed_words.insert(0, given_string[word_present_index:word_ending_index + 1])
    
    return ' '.join(reversed_words)

print(reverse_words_in('Alice likes Bob'))



