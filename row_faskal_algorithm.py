
# row faskal algorithm 

def row_pascal_algorithm(n):
    if n <= 0:
        return []

    result = [[1]]

    for _ in range(1, n):
        prev_row = result[-1]
        new_row = [1]

        for i in range(1, len(prev_row)):
            new_row.append(prev_row[i - 1] + prev_row[i])

        new_row.append(1)
        result.append(new_row)

    return result

def print_pascal_triangle(triangle):
    for row in triangle:
        print(row)

n = 5
pascal_triangle = row_pascal_algorithm(n)
print_pascal_triangle(pascal_triangle)



# ---------- i tried this far below

#### above evoluteioned by this

# row faskal algorithm 

# def row_faskal_algorithm():
#     array = [1, 1]
#     enter_the_number = 5
#     for item in range(enter_the_number-2):
#         array = [1] + calculate(array) + [1]
#         print(array)
#     #return array


# def calculate(array):
#     for item in range(len(array)-1):
#         array[item] = array[item] + array[item+1]
#     return array[:len(array)-1]
        

    
# print(row_faskal_algorithm())














