# 시간을 초 단위로 입력하세요 : 6543
# 6543초는 1 시간 49 분 3 초입니다

초 = 6543
한시간은몇초 = 3600
시간 = 초//한시간은몇초

나머지분 = 6543-3600
일분은몇초 = 60
분 = 나머지분//60
몇초 = 나머지분%60

print(초,'초는 ' , end= '')
print(시간,'시간 ' ,end='')
print(분,'분 ' ,end='')
print(몇초,'초입니다')



