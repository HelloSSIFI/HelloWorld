
# 세그먼트 트리 중 구간합 트리를 구하는 방법 활용하기 
# -> 구간합이 아닌 '부분합'이므로 세그먼트 트리 방법은 부적합

def init(start, end, node):
    '''
    구간합 트리 구성
    start: 시작 인덱스
    end: 끝 인덱스
    node: 현재 노드 인덱스
    '''
    global min_length, S

    length = end - start + 1
    if start == end:
        if numbers[start] >= S:
            min_length = min(min_length, length)
        return numbers[start]

    mid = (start + end) // 2
    tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1)
    if tree[node] >= S:
        min_length = min(min_length, length)
    return tree[node]


N, S = map(int, input().split())
numbers = list(map(int, input().split()))
tree = [0 for _ in range(101 ** 2 * 2 + 1)]     # 최대 N의 범위 보다 큰 범위의 수에서 x2
min_length = N + 1
init(0, N-1, 1)
print(tree)
print(min_length)
