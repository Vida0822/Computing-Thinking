#3

Sh=int(input('새우깡 구매 개수 : '))
Bi=int(input('비비빅 구매 개수 : '))
Cho=int(input('초코파이 구매 개수 :'))
mat=int(input('맛동산 구매 개수: ' ))

print('======================')

a,b,c,d=Sh*1200,Bi*400,Cho*500,mat*1500

print('새우깡 구매 금액     : %d' %(a))
print('비비빅 구매 금액     : %d' %(b))
print('초코파이 구매 금액  : %d' %(c))
print('맛동산 구매 금액     : %d' %(d))

print('======================')

print('총 구매 금액           :%d' %(a+b+c+d))
