def decimal_to_r_notation(number, r):
    
    number_front = int(number)
    number_rear = number - number_front

    remainder_list = []      
   
    while True:
        quotient = divmod(number_front, r)[0]  
        remainder = divmod(number_front, r)[1]   
        remainder_list.append(remainder)
        if quotient == 0: break
        else:
            number_front = quotient
   
    remainder_list.reverse()
   
    result_front = ""
    for digit in remainder_list:
        result_front += str(digit)


    integer_part_list = []
    c = 6
    if number_rear == 0:
        return result_front

    while c != 0:
        c = c - 1
        integer_part = int(number_rear * r)
        decimal_part = number_rear * r - integer_part
        integer_part_list.append(integer_part)
        if decimal_part == 0: break
        else:
            number_rear = decimal_part

    result_rear = ""
    for digit in integer_part_list:
        result_rear += str(digit)

    result = result_front + "." + result_rear
    return result


if __name__ == "__main__":
    number = input("input the number : ")
    r = input("input the radix : ")
    print(decimal_to_r_notation(float(number),int(r))+"("+ r +")")
