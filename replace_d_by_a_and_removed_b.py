
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









