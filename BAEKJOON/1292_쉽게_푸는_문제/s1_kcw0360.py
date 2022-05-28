A, B = map(int, input().split())

sequence = [0]
num = 0
while len(sequence) - 1 < B:
    num += 1
    for i in range(num):
        sequence.append(num)

print(sum(sequence[A:B+1]))




