def solution(numbers):
    answer = []
    for num in numbers:                                     # 2진수로 바꾸고 오른쪽부터 봤을 때 가장 먼저 0이 나오는 지점을 찾아 1로 바꾸고
        i = 0                                               # 해당 지점부터 다시 오른쪽으로 가면서 1이 나오는 부분이 있다면 0으로 바꿔주면 조건을 만족
        while num & (1 << i): i += 1                        # 오른쪽부터 0이 나오는 지점을 i로 찾음

        num ^= 1 << i                                       # 해당 지점을 1로 바꾸고
        i -= 1                                              # i의 오른쪽부터
        while i > 0 and num & (1 << i) == 0: i -= 1         # i가 음수가 아닐 때까지 오른쪽으로 이동하면서 1이 나오는 지점을 찾음
        if i >=0: num ^= 1 << i                             # 만약 i가 음수가 아니면서 1인 지점이 있다면 0으로 바꿔줌

        answer.append(num)
    return answer


# print(solution([2, 7]))
