
# inter conversion of string and integer

def inter_conversion_of_integer_and_string():

    user_input = input("enter the string or integer : ")

    if user_input[0] != '"':
        return f'string : {str(user_input)} , type : {type(user_input)}'
    
    user_input = int(user_input[1:len(user_input)-1])
    return f'value : {user_input} , type: {type(user_input)}'


print(inter_conversion_of_integer_and_string())


#   sample input 

#   123456789 , "1234566789"
