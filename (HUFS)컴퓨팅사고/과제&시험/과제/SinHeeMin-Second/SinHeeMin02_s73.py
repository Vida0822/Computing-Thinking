# Self study 7-3


List1= [ ]
List2= [ ]
value =0

for i in range (0,4):
    for j in range(0,5):
        List1.append(3*value)
        value+=1
    List2.append(List1)
    List1= [ ]

for j in range (0,4):
    for k in range (0,5):
        print('%3d' % List2[ j ] [ k ]  , end= ' ')
    print(' ')
        
