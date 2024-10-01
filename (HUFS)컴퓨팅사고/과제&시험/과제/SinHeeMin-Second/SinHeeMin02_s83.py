#Self study 8-3

Ho=input('문자열 입력:')

if Ho.isalpha( ) == True:
    print('글자입니다')

elif Ho.isdigit( ) == True:
    print('숫자입니다')

elif Ho.isalnum() == True:
    print('글자 + 숫자입니다')

else:
    print('모르겠습니다')
