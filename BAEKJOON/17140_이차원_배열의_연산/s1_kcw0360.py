import sys
input = sys.stdin.readline


r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]
answer = 0
len_r, len_c = 3, 3


def cal(length):
    for i in range(len(arr)):    # 행을 순서대로 체크
        temp = []
        for j in set(arr[i]):    # 중복제거
            if j:    # 0이 아닌 수만 카운트
                temp.append([j, arr[i].count(j)])    # [숫자, 개수] 형태로 temp에 추가

        temp.sort(key=lambda x: (x[1], x[0]))    # 개수로 정렬한 후, 숫자로 정렬

        if len(temp) > 50:    # r, c의 최대값이 100이기 때문에 temp 길이가 50이 넘는다면 50개 까지 자른다.
            temp = temp[:50]

        arr[i] = []    # 현재 행 초기화
        for a, b in temp:    # 숫자 개수 순으로 넣어준다.
            arr[i].append(a)
            arr[i].append(b)

        length = max(length, len(arr[i]))    # 행의 최대 길이 저장

    for i in range(len(arr)):    # 최대 길이 보다 길이가 작은 경우 부족한 만큼 0을 채운다.
        check = len(arr[i])
        if check < length:
            arr[i] += [0] * (length - check)

    return length


flag = False
while answer < 101:
    if r <= len_r and c <= len_c and arr[r-1][c-1] == k:    # r, c가 현재 배열의 idx 범위에 들어오는 경우 k값이 맞는지 확인
        flag = True
        break

    if len_r >= len_c:    # 행이 열보다 길이가 크거나 같은 경우
        len_c = cal(len_c)    # 열의 길이 재설정
    else:    # 열이 행보다 길이가 크거나 같은 경우
        arr = list(zip(*arr))    # 연산을 위해 행과 열을 바꿔준다.
        len_r = cal(len_r)    # 행의 길이 재설정
        arr = list(zip(*arr))    # 배열을 원래대로 돌려 놓는다.

    answer += 1

if flag:
    print(answer)
else:
    print(-1)