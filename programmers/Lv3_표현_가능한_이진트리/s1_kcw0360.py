def binary(num):
    temp = []
    while True:    # 2진수로 변환
        a, b = divmod(num, 2)
        temp.insert(0, b)

        if a != 0:
            num = a
        else:
            break

    res = ''.join(map(str, temp))

    length = len(res)
    cnt = 1    # 이진트리 높이
    while True:    # '0'을 추가하여 이진트리 높이만큼 포화 이진트리가 되도록 글자 수 맞춰주기
        if length > (2 ** cnt - 1):
            cnt += 1
        else:
            break

    ln = 2 ** cnt - 1
    if length != ln:
        res = '0' * (ln - length) + res

    return res


def check(num, now, end):    # 중위 순회(Inorder Traversal)로 이진 트리 확인
    if now == end:    # 해당 노드에 도착한 경우 문자열에서 노드에 해당 하는 값 리턴
        return num[now]

    mid = (now + end) // 2

    # 이미 False 값이 리턴 되었거나 부모가 더미 노드('0) 인데 자식이 더미 노드가 아닌 경우 False 리턴
    left = check(num, now, mid - 1)
    if not left or (num[mid] == '0' and left == '1'):
        return False

    right = check(num, mid + 1, end)
    if not right or (num[mid] == '0' and right == '1'):
        return False

    if num[mid] == '0' and left == '0' and right == '0':    # 부모, 자식 모두가 '0'인 경우는 '0'을 리턴
        return '0'

    return '1'    # 부모, 자식 모두가 '1'인 경우 '1'을 리턴


def solution(numbers):
    answer = []
    for number in numbers:
        bin_num = binary(number)

        if check(bin_num, 0, len(bin_num) - 1):
            answer.append(1)
        else:
            answer.append(0)

    return answer