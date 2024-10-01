#5

import random

print('번호   국어    영어   수학')
print('-----------------')

List1=[ ]
List2=[ ]

for i in range (0,10):
    for j in range(0,3):
        a=int(random.randrange (1,100))
        List1.append(a)
    List2.append(List1)
    List1=[ ] 

for k in range(0,10):
    print(k+1,end='     ')
    for p in range(0,3):
        print('%d' %List2[k][p], end='     ')
    print(' ')
        


        
