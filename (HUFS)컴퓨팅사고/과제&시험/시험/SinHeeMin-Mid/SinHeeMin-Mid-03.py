
#3

import random
computer=random.randrange (1,3)
user=int(input('가위, 바위, 보를 선택하세요. \n1. 가위, 2.바위, 3. 보:'))

if computer > user:
    print('컴퓨터:승, 사용자:패')
elif computer < user:
    print('컴퓨터: 패, 사용자:승')
else:
    print('무승부')

print('사용자:%d \n컴퓨터: %d' %(user, computer))
