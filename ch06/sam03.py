n= int(input('정수를 입력하세요'))
result=1
for i in range(n,0,-1):
    result=result*i
print(n,'펙토리얼의 값은',result,'입니다')
