def solution(arr1, arr2):
    column = len(arr1)
    share = len(arr1[0])
    row = len(arr2[0])

    answer = [[0]* row for i in range(column)]

    for a in range(column):
        for b in range(share):
            for c in range(row):
                answer[a][c] += arr1[a][b] * arr2[b][c]

    return answer