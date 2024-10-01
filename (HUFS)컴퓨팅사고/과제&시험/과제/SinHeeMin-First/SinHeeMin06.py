#교재 05장 127p SELF STUDY 5-2


#문제: 두 숫자를 입력받고 두 숫자 사이의 합계를 구하는 프로그램을 만들어보자. 단 증가하는 숫자도 입력 받는다.

a=0
b=0
c=0
Sum=0

a=int(input('첫 번째 숫자를 입력하세요'))
b=int(input('두 번째 숫자를 입력하세요'))

if a>b:
    print('두번째 숫자는 첫번째 숫자보다 커야합니다')

else:
    c=int(input('더할 숫자를 입력하세요'))
    for num in range (a,b+1,c):
        Sum =Sum+num

    print('%d + %d + ...+ %d는 %d입니다. ' %( a, a+c, b ,Sum))
