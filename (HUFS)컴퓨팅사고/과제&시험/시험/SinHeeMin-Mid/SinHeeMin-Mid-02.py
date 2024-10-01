
#2

price=int(input('물건값을 입력하시오:'))

천원=int(input('1000원 지폐개수:'))
오백원=int(input('500원 동전 개수:'))
백원=int(input('100원 동전 개수:'))

exchange=천원*1000+오백원*500+백원*100-price

c1= exchange//500
exchange%=500

c2=exchange//100
exchange%=100

c3=exchange//10
exchange%=10

print('500원 = %d 100원 = %d 10원 = %d 1원=%d' %(c1,c2,c3,exchange))  
