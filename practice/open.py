with open('alice_assignment.txt', 'r', encoding='utf-8') as f:
    data = f.read()


chars = len(data)
words = len(data.split(' '))
lines = len(data.split('\n'))


print("총 글자 수:", chars)
print("총 단어 수:", words)
print("총 줄 수:", lines)