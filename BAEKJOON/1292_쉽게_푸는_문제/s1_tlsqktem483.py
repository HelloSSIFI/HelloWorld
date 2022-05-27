A, B = map(int, input().split())
arr = [0]
for i in range(46):
    for j in range(i):
        arr.append(i)
print(sum(arr[A:B+1]))