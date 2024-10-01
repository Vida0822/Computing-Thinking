
#5

print('===원리금 계산 프로그램===')

money=int(input('저축금액을 입력하시오.:'))

interest=int(money*0.0375)
tex=int(interest*0.15)
final=money+interest-tex

print('원금:    {0:,} \n이자:       {1:,} \n세금:         {2:,}\n최종:    {3:,}\n' .format(money,interest,tex,final))

