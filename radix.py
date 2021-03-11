def decimal_to_r_notation(number, r):
    '''
    10진수를 입력받아서 r 진수(r=2, 8, 16, ...)로 변환하는 함수
    '''
    # 소수점 앞의 정수 부분과, 소수점 뒤의 소수 부분을 구분
    number_front = int(number)
    number_rear = number - number_front      
     
    ### 정수 부분 r 진수 변환
    # n을 r로 나눈 나머지를 담는 list
    remainder_list = []      
   
    while True:
        #divmod(n, r)는 n을 r로 나눈 값을 (몫, 나머지) tuple로 반환
        quotient = divmod(number_front, r)[0]  
        remainder = divmod(number_front, r)[1]   
        # 나머지를 결과 list에 추가
        remainder_list.append(remainder)
        # 몫이 0이면 반복문 탈출
        if quotient == 0: break
        # 몫이 0이 아니면, 몫을 다시 r로 나누는 과정을 반복
        else:
            number_front = quotient
   
    # remainder_list 원소 배열 순서를 거꾸로 뒤집는다
    remainder_list.reverse()
   
    # remainder_list 배열의 원소를 하나의 string으로 변환 (정수 부분 result_front)
    result_front = ""
    for digit in remainder_list:
        result_front += str(digit)

          
    ### 소수 부분 r 진수 변환
   
    # 소수 부분에 r을 곱한 결괏값 중 정수 부분을 담는 list
    integer_part_list = []
    c=6
    while c!=0:
        c=c-1
        # 소수 부분에 r을 곱한 값 중 정수만을 따로 list에 담는다. 소수 부분이 0이 될 때까지 반복한다
        integer_part = int(number_rear * r)
        decimal_part = number_rear * r - integer_part
        integer_part_list.append(integer_part)
        if decimal_part == 0: break
        else:
            number_rear = decimal_part

    # integer_part_list 배열의 원소를 하나의 string으로 변환 (정수 부분 result_rear)
    result_rear = ""
    for digit in integer_part_list:
        result_rear += str(digit)

    # 정수 부분 result_front, 소수 부분 result_rear를 소수점(.)과 결합
    result = result_front + "." + result_rear
    return result


if __name__ == "__main__":
    number = input("input the number : ")
    r = input("input the radix : ")
    print(decimal_to_r_notation(123.456456,7))
    print(decimal_to_r_notation(float(number),int(r))+"("+ r +")")
