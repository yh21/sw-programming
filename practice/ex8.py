scores = input("여러개의 점수를 입력하시오>").split(' ')
for i in range(len(scores)):
    scores[i] = int(scores[i])
print(sum(scores))