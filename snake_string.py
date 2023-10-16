
# return a snake or sinusoidal string 

#  example:    hello_world

##     e             _              l

##   h     l      0     w       r       d

###            l             o



def snake_string(string):
    first_bit  = 0
    second_bit = 1
    theird_bit = 3
    length_of_string = len(string)-1
    snake_string_sequence = []

    for _ in range(len(string)):
        if second_bit <= length_of_string:
            snake_string_sequence.append(string[second_bit])
            second_bit += 4

        elif first_bit <= length_of_string:
            snake_string_sequence.append(string[first_bit])
            first_bit += 2

        else:  #   theird_bit <= length_of_string:first_bit
            snake_string_sequence.append(string[theird_bit])
            theird_bit += 4

    return ''.join(snake_string_sequence)


print(snake_string('Hello_world!'))












