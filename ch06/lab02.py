count=0#시도횟수
import random
compNo = random.randint(1,100)
userNo=0#사용자의 초기값

while compNo !=userNo:
    userNo=int(input('1~100까지의 숫자를 입력하세요'))
    if compNo>userNo:
        print('입력한 숫자보다 큽니다')
    elif compNo<userNo:
        print('입력한 숫자보다 작습니다')
    else:
        print('축하합니다 맞췄습니다')
        
    count=count+1
print(count,'번 만에 맞추셨습니다')
