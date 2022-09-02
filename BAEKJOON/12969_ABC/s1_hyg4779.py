import sys
imput = sys.stdin.readline


def dfs(a, b, length, total):

    if length == n:
        if total == k:
            print(''.join(arr))
            exit()
        else:
            return

    # 체크 안해본 문자열이면 True / 햇으면 return
    if not dp.get((a, b, length, total), default=False):
        dp[(a, b, length, total)] = True
    else:
        return

    # A보다 작은 순서쌍은 없으니 total 그대로
    arr[length] = 'A'
    dfs(a + 1, b, length + 1, total)

    # B는 A보다 크니까 A수 만큼 total+
    arr[length] = 'B'
    dfs(a, b + 1, length + 1, total + a)

    # C는 A, B 보다 크니까 A+B수 만큼 total+
    arr[length] = 'C'
    dfs(a, b, length + 1, total + a + b)


n, k = map(int, input().rstrip().split())
dp = dict()
arr = [0] * n

dfs(0, 0, 0, 0)
print(-1)