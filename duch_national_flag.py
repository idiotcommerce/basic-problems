
# duch national flag. 

def duch_national_flag(flag):

       

    small_item, mid_item = 0 , 0
    high_item = len(flag) - 1

    for _ in range(len(flag)):

        if flag[mid_item] == 0:
            flag[small_item], flag[mid_item] = flag[mid_item], flag[small_item]
            small_item += 1
            mid_item += 1

        elif flag[mid_item] == 1:
            mid_item += 1

        else :
            flag[mid_item], flag[high_item] = flag[high_item], flag[mid_item]
            high_item -= 1
            
    return flag

print(duch_national_flag( [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1] ))



