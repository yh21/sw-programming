time = int(input('초 단위 시간을 입력하세요: '))

minute = time // 60
second = time % 60

print(">>", minute, '\b분', second, '\b초 입니다!')