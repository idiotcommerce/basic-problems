
# finding prime numbers in 


def find_prime_numbers(N):
    prime_list = [2]
    for number in range(3,N+1):
        if not has_factors(number):
            prime_list.append(number)
    return prime_list
    
def has_factors(number):
    check_factors_upto = (number // 2) + 1
    for i in range(2, check_factors_upto):
        if number % i ==0 :
            return True
    return False

print(find_prime_numbers(100))








