'''
왜 : 옆에 띄어쓰기를 하나요? --> 문자열임
꼭 띄어쓰기 안해도 괜찮음요

a = input('이름을 입력해주세요: ')
print(a)

array = [1, 2, 3]
print(array)


print("life", "is", "too short", end=" ---> ")
print("I", "want", "Food")

print("유지", "지선", "유진", "진규", "령현",sep='님 ') #,sep 여기에는 왜 띄어쓰기 안하나요ㅠㅠ

print("유지", "지선", "령현", "유진", "진규",sep='님 ',end='')
print("님")
'''

a = input('이름을 입력해주세요:')
print("이름: ", end="")
print(a)
b = input('파트를 입력해주세요:')
print("소속 파트: ", end='')
print(b)
c = input('어느 기수 입니까?:')
print("기수: ",end='')
print(c)
d = input('OB입니까 YB입니까?: ')
print('저는: ',end='')
print(d, end='입니다.')
