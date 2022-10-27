N = 10**9


class Node:
    # 활성, 비활성
    live = True

    # 이전 노드와 다음 노드
    def __init__(self, p, n):
        self.prev = p if p >= 0 else None
        self.next = n if n < N else None


def solution(n, k, camaand):
    global N
    N = n

    # linked list
    table = {i: Node(i-1, i+1) for i in range(n)}

    # 현재 선택된 행
    now = k

    # 삭제된 번호
    stack = []


    for cmd in camaand:
        # 삭제
        if cmd[0] == 'C':
            # 비활성
            table[now].live = False
            stack.append(now)

            prev, next = table[now].prev, table[now].next

            # 이전 노드가 있다면 현재 노드의 다음 노드와 연결
            if prev is not None:
                table[prev].next = next

            # 다음 노드가 있다면 이전 노드를 다음 노드와 연결
            if next is not None:
                table[next].prev = prev

            # 다음 노드가 없다면 이전 노드 선택, 아니면 다음 노드 선택택
            if table[now].next is None:
                now = table[now].prev
            else:
                now = table[now].next

        # 복구
        elif cmd[0] == 'Z':
            # 활성
            re = stack.pop()
            table[re].live = True

            prev, next = table[re].prev, table[re].next

            # 이전 노드가 있다면 복구 행과 이전노드 연결
            if prev is not None:
                table[prev].next = re

            # 다음 노드가 있다면 복구 행과 다음 노드 연결
            if next is not None:
                table[next].prev = re


        else:
            c, amout = cmd.split()
            # 위
            if c == 'U':
                # 연결된 이전 노드로 계속 변경
                for _ in range(int(amout)):
                    now = table[now].prev

            # 아래
            else:
                # 연결된 다음 노드로 계속 이동
                for _ in range(int(amout)):
                    now = table[now].next

    return ''.join('O' if table[i].live else 'X' for i in range(n))

print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))