
# reverse words in string

# Solution 1 :

def reversed_string(string):

    words = string.split()
    reversed_words = reversed(words)
    reversed_string = ' '.join(reversed_words)
    return reversed_string

print(reversed_string('Alice likes Bob'))


# Solution 2 


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









