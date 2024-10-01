#4


score={'파이썬' : 'A', '자바' : 'B+', '컴퓨터개론' : 'C', '확률과 통계' : 'A+', '기초영어' : 'F','언어학' : 'C+'}

print('#시나리오1' , score,'\n')


print('#시나리오2')
print('자바 : %s' %(score.get('자바')))
print('언어학 : %s' %(score.get('언어학')))
print('\n')


print('#시나리오3')
score['C/C++' ] = 'A'
score['기초 일본어'] = 'A+'
print(score,'\n')


print('#시나리오4')
score['자바'] = 'F'
score['언어학'] = 'A'
print(score,'\n')


print('#시나리오5')
print(score 
