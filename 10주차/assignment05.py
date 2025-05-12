import random

print('''
------------------------
컴퓨터가 알려주는 행운의 로또번호
------------------------
      ''')
print('아무키나 누르면 추첨을 시작합니다')
input()

luckybox = []
count = 0

while count < 6:
    num = random.randint(1, 46)
    if num in luckybox:
        pass
    else:
        luckybox.append(num)
        count += 1

print('이번주 행운의 번호는', luckybox, '입니다.')
