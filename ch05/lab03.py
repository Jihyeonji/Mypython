login_id=input('ID를 입렵하세요')
pwd=input('암호를 입력하세요')
com_id='Korea'
com_pwd='baseball'

if login_id == com_id and pwd == com_pwd:
    print('로그인 성공')
    elif login_id == com_id and pwd != com_pwd:
        print('암호가 틀렸습니다')
else :
    print('존재하지 않는ID입니다')
