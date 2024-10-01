
#1

attand= int(input("출석 점수:"))
assignment= int(input('과제 점수:'))
middle=int(input('중간고사 점수:'))
final = int(input('기말고사 점수:'))

Sum=attand*0.1+assignment*0.2+middle*0.3+final*0.4
print('당신의 최종점수는 %.1f점 입니다.' %(Sum))

if 0<=Sum<70:
    print('70점 미만이므로 FAIL입니다.')
elif 70<=Sum <=100:
    print('70점 이상이므로 PASS입니다.')
else:
    print('잘못된 점수입니다')


