import random

print("-" * 30)
print("2025 뉴 가위 바위 보 게임")
print("-" * 30)

while True:
    player = input("가위, 바위, 보 중에 하나를 입력하세요 > ")
    computer = random.choice(['가위', '바위', '보'])

    print(">> 플레이어:", player, "\t컴퓨터:", computer)

    if player == computer:
        print("비겼습니다.")
    elif (player == "가위" and computer == "보") or \
         (player == "바위" and computer == "가위") or \
         (player == "보" and computer == "바위"):
        print("You Win~!")
        print("-" * 30)
        print("2025 뉴 가위 바위 보 게임")
        print("-" * 30)
    else:
        print("You Lose 🤣")
        break