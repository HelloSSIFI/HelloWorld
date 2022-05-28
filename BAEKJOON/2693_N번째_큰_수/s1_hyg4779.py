def q_sort(args):
    if len(args) <= 1:
        return args

    pivot = args[0]
    tail = args[1:]

    left = [x for x in tail if x<= pivot]
    right = [x for x in tail if x> pivot]

    return q_sort(left) + [pivot] + q_sort(right)


arr = [list(map(int, input().split())) for _ in range(int(input()))]
for x in range(len(arr)):
    tmp = q_sort(arr[x])
    print(tmp[-3])
