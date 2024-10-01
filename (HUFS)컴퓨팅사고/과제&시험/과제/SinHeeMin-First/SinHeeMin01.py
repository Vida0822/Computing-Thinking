#교재 2장 58p 연습문제 7번 - 파일 01



#문제: 정수 2개를 입력 받아서 더하기, 곱하기, 제곱 연산을 하는 프로그램을 작성하시오.


a=int(input('숫자1 입력:' ))
b=int(input('숫자2 입력:'))

print('%d +%d = %d'  %(a,b,a+b))
print('%d * %d = %d' %(a,b,a*b))
print('%d ^ %d = %d' %(a,b,pow(a,b)))

