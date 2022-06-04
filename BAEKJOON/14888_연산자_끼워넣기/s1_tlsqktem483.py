"""
DFS 이용 풀이
시간 : 132 ms
"""

N = int(input())
numbers = list(map(int, input().split()))
operations = list(map(int, input().split()))
ans = []

def operation(sum, n_list, o_list):
    if not n_list:
        ans.append(sum)
        return

    for idx, op in enumerate(o_list):
        temp = o_list[:]
        if op:
            temp[idx] -= 1
            if idx == 0:
                operation(sum + n_list[0], n_list[1:], temp)
            elif idx == 1:
                operation(sum - n_list[0], n_list[1:], temp)
            elif idx == 2:
                operation(sum * n_list[0], n_list[1:], temp)
            else:
                operation(int(sum / n_list[0]), n_list[1:], temp)

operation(numbers[0], numbers[1:], operations)
print(max(ans))
print(min(ans))
