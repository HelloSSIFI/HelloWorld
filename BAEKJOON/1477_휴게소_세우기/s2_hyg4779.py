n, m, l = map(int, input().split())

# 시작지점과 끝지점 삽입
spots = [0]+list(map(int, input().split()))+[l]
spots.sort()

s, e = 1, l-1
answer = 0

while s <= e:
    mid = (s+e)//2
    count = 0

    # mid보다 거리가 벌어진 위치만 휴게소를 세운다
    for i in range(1, n+2):
        if spots[i]-spots[i-1] > mid:
            count += (spots[i]-spots[i-1]-1)//mid


    # 원래 지으려던 것보다 많이 지었으면 s를 늘린다
    if count > m:
        s = mid+1

    # 원래 지으려던 것보다 적거나 같게 지었으면 e를 당긴다
    else:
        e = mid-1
        answer = mid

print(answer)