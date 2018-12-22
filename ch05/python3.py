alist=['이순신',25,'abc',3.5]
for a in alist:
    print(a)
print(alist[1:3])
print(alist[:3])
print(alist[1:])
print(alist[-3:] )
print(alist[-1])

alist.append('대한민국')
print(alist)

blist=['대한민국','중국','일본','미국','베트남']
print(blist)
blist.append('호주')
print(blist)
clist=[56,29,134,333]
clist.append(24)
print(clist)
print(type(clist))
