in_money=int(input('투입한 금액'))
price=int(input('물건값'))
change=in_money-price
coin500=change//500
coin100=(change%500)//100
remain=change-coin500*500-coin100*100 
print('거스름돈:',change)
print('500원 동전의 숫자:',coin500)
print('100원 동전의 숫자:',coin100)
print('완전잔돈:',remain,'원')
