def solution(k, ranges):
    answer = []
    arr = [k]

    while k != 1:

        if k % 2:
            k = k*3 + 1
        else:
            k //= 2

        arr.append(k)

    for a, b in ranges:
        temp = len(arr) + b - 1
        if a > temp:
            answer.append(-1)
        else:
            t = 0
            for i in range(a, temp):
                t += (arr[i]+arr[i+1])/2
            answer.append(t)

    return answer