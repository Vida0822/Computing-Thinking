#교재 05장 127p SELF STUDY 5-1


#문제: 성적을 입력받고 A+에서 F까지 세분화해보시오


score= int(input('점수를 입력하세요'))


if 95<=score and score<=100:
    print('A+')
elif 90<=score and score<95:
    print('A0')
elif 85<=score and score <90:
    print('B+')
elif 80<=score and score <85:
    print('B0')
elif 75<=score and score <80:
    print('C+')
elif 70<=score and score <75:
    print('C ')
elif 65<=score and score <70:
    print('D+')
elif 60<=score and score <65:
    print('D')
elif 0<=score and score <60:
    print('F ')
    
print('학점입니다^^')



