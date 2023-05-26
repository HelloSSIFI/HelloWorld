import sys
sys.setrecursionlimit(10**6)


def divide(arr):
    node = arr[0]
    left, right = [], []

    for i in range(1, len(arr)):    # 현재 노드의 x좌표 기준으로 자식노드를 좌, 우 리스트로 분류
        if node[0] > arr[i][0]:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return left, node, right

def preorder(arr, result):
    left, node, right = divide(arr)    # 현 위치를 기준으로 좌, 우에 있는 노드들 찾기

    result.append(node[2])    # result 현 위치 번호 추가 후 순회

    if len(left) > 0:
        preorder(left, result)

    if len(right) > 0:
        preorder(right, result)

    return

def postorder(arr, result):
    left, node, right = divide(arr)

    if len(left) > 0:
        postorder(left, result)

    if len(right) > 0:
        postorder(right, result)

    result.append(node[2])    # 순회가 끝난 후 현 위치 번호 추가 (순회 마다 현 위치를 추가 해주는 위치가 다르니 주의)

    return

def solution(nodeinfo):
    pre_ans = []    # 전위 순회 결과
    post_ans = []    # 후위 순회 결과

    for i in range(len(nodeinfo)):    # 좌표에 노드 번호 추가
        nodeinfo[i].append(i+1)

    arr = sorted(nodeinfo, key=lambda x: (-x[1], x[0]))    # y좌표, x좌표 기준 순으로 정렬

    preorder(arr, pre_ans)    # 전위 순회
    postorder(arr, post_ans)    # 후외 순회

    return [pre_ans, post_ans]