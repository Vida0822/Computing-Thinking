# Self study  6-5

num1 = int(input('시작값을 입력하세요:'))
num2 = int(input('끝값을 입력하세요: '))
num3 = int(input('증가값을 입력하세요:'))

total = 0
a=num1

while num1 <= num2:
    total+=num1
    num1+=num3
    

print('%d에서 %d까지 %d씩 증가시킨 값의 합계 : %d' %(a,num2,num3,total))
    
