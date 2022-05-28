N, M = map(int, input().split())

arr = list()


def recur(n):
    tmp = 0
    while len(arr) < n:
        tmp += 1
        cnt = 0
        while cnt != tmp:
            arr.append(tmp)
            cnt += 1

recur(M)

print(sum(arr[N-1:M]))