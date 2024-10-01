#1

print('정수 A부터 B까지 더하는 프로그램')
print('------------------------')

A=int(input('정수 A 입력: '))
B=int(input('정수 B 입력: '))
Sum=0

if A<=B:
    for i in range (A,B+1):
        Sum+= i
        
    print('%d부터 %d까지 더한 값: %d' %(A,B,Sum))
    
else:
    print('잘못된 수가 입력되었습니다.\n프로그램을 종료합니다.' )
    



    
