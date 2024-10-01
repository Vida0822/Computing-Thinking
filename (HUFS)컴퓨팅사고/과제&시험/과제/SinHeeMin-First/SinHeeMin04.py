#교재 5장 135p 연습문제 7번 - 파일 04


#문제: 두 사람이 주사위를 던져 더 큰수가 나오면 이기는 게임이다. A가 이기거나 B가 이기거나 비기는 결과가 나와야 한다. 코드를  작성하시오

import random

a= random.randrange (1,7)
b= random.randrange (1,7)

print('A의 주사위 숫자는 %d입니다' %(a))
print('B의 주사위 숫자는 %d입니다' %(b))

if a>b:
    print('A가 이겼습니다.')
elif a<b:
    print('B가 이겼습니다.')
else:
    print('비겼습니다')


