import sys
input = sys.stdin.readline


R, C, M = map(int ,input().split())
sharks = dict()
catch = []
for _ in range(M):                                          # sharks 딕셔너리에 key=좌표, value=정보를 담아줌
    r, c, s, d, z = map(int, input().split())
    sharks[(r - 1, c - 1)] = (s, d, z)

for i in range(C):                                          # 낚시왕의 위치를 i로 표시
    candi = [(R, i, 0, 0, 0), 0]                            # 낚시왕이 잡을 물고기 후보 [이전위치, 새로운위치]
    
    new_sharks = dict()                                     # 이동한 상어들의 위치와 정보를 담아줄 딕셔너리
    for r, c in sharks:                                     # 상어들의 정보를 순회
        s, d, z = sharks[(r, c)]
        a = 1
        if d in [1, 4]:
            a = -1
        
        if d in [1, 2]:                                     # 조건에 맞게 이동한 좌표를 nr, nc
            nr = (r + s * a) % ((R - 1) * 2)                # 그 때 바라보는 방향을 nd로 저장
            nd = d
            if nr > R - 1:
                nr = (R - 1) * 2 - nr
                nd = (d % 2) + 1
            nc = c
        else:
            nr = r
            nc = (c + s * a) % ((C - 1) * 2)                # 현재 상어가 낚시왕이 잡을 열에 있고 행번호가 더 작다면
            nd = d                                          # 이전 후보군에 있는 상어를 new_sharks에 넣어줌 
            if nc > C - 1:                                  # 이 때 이미 같은 자리에 상어가 있다면
                nc = (C - 1) * 2 - nc                       # 크기가 더 큰 상어만 남겨놓음
                nd = (d % 2) + 3                            # 낚시 후보군이 아니라면 new_sharks에 있는지 확인 후 큰 상어를 저장

        if c == i and r < candi[0][0]:
            if candi[1]:
                key = (candi[1][0], candi[1][1])
                if not new_sharks.get(key) or new_sharks[key][2] < candi[1][4]:
                    new_sharks[key] = (candi[1][2], candi[1][3], candi[1][4])
            
            candi = [(r, c, s, d, z), (nr, nc, s, nd, z)]
        
        else:
            if not new_sharks.get((nr, nc)) or new_sharks[(nr, nc)][2] < z:
                new_sharks[(nr, nc)] = (s, nd, z)
    
    catch.append(candi[0][4])
    sharks = new_sharks

print(sum(catch))
