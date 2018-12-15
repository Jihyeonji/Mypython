americano=2000
cafelatte=3000
capucino=3500
ame_no=int(input('오늘 판매한 아메리카노의 숫자는'))
latte_no=int(input('오늘 판매한 카페라떼의 숫자는'))
capu_no=int(input('오늘 판매한 카푸치노의 숫자는'))

ame_sum=americano*ame_no
latte_sum=cafelatte*latte_no
capu_sum=capucino*capu_no

all_sum=ame_sum+latte_sum+capu_sum
print('총매출은',all_sum,'원입니다')
 
