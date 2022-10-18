def search(n):
    global answer
    if len(child[n]) == 0:                                      # 자식이 없다면
        answer += 1                                             # 결과 +1 후 리턴
        return

    if len(child[n]) == 1 and child[n][0] == deleted:           # 자식이 하나인데 제거된 자식이면
        answer += 1                                             # 결과 +1 후 리턴
        return

    for i in child[n]:                                          # 자식 노드를 순회하면서
        if i == deleted:                                        # 제거된 자식이면 건너뛰고 재귀
            continue
        search(i)


N = int(input())
parent = list(map(int, input().split()))
child = [[] for _ in range(N)]
deleted = int(input())
root = 0
for i in range(N):
    if parent[i] == -1:                                         # 부모가 -1 이면 루트 노트로 설정
        root = i
        continue
    child[parent[i]].append(i)

if deleted == root:                                             # 루트 노드가 제거되었다면
    print(0)                                                    # 0 출력 후 프로그램 종료
    exit()

answer = 0
search(root)                                                    # 루트노드를 넣고 탐색
print(answer)
