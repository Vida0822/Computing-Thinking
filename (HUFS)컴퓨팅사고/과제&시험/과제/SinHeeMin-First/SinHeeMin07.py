
#7. 교재 05장 127p SELF STUDY 5-3



#문제: 숫자를 하나 입력받고, 그 숫자가 소수인지 체크하는 프로그램을 만들어보자.


num=int(input('숫자를 하나 입력하세요'))

if num>1:
    for a in range (2,num,1):
        if num%a==0:
            print('%d는 소수가 아닙니다' %(num))
            break
        
        else:
            if a==num-1:
                print('%d는 소수입니다.' %(num))

else:
    print('%d는 소수가 아닙니다.' %(num))
