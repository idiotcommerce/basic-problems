
# palendrum 

def palendrum_validation(query):

    if query == query[::-1]:
        return f" {query} is a palendrum"
    return f' {query} not a palendrum'

print(palendrum_validation(str(input())))


# ======================================
# =======================================


def validate_palendrum(query):

    pelendrum_length = len(query)-1
    for i in range(pelendrum_length):

        if query[pelendrum_length] != query[i]:
            pelendrum_length -= 1
            return f' {query} is not a palendrum '
        
        return f' {query} is palendrum '

    
print(validate_palendrum(str(input())))















