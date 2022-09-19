N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
answer = 100 * N * N

for x in range(N - 2):                                                                          # 기준점 x, y
    for y in range(1, N - 1):
        for d1 in range(1, N // 2):                                                             # 경계의 길이 d1, d2
            if y - d1 < 0 or x + d1 >= N:
                break
            for d2 in range(1, N // 2):
                if y + d2 >= N or x + d1 + d2 >= N:                                             # 경계가 격자를 넘어서면 continue
                    break

                population = [0] * 5                                                            # 각 경계구의 인구를 더해줄 리스트
                for r in range(N):                                                              # 모든 격자를 탐색
                    for c in range(N):
                        r_min = max(x - c + y, x + c - y)                                       # 우선 5번 구역을 정해줌
                        r_max = min(x + d1 + c - y + d1 + 1, x + d2 + 1 - c + y + d2)           # 문제 조건대로 구역을 계산

                        c_min = max(y - r + x, y - d1 + r - x - d1)
                        c_max = min(y + r - x + 1, y + d2 + 1 - r + x + d2)

                        if r_min <= r < r_max and c_min <= c < c_max:                           # 5번 구역 먼저 배치 후
                            population[4] += area[r][c]

                        elif 0 <= r < x + d1 and 0 <= c <= y:                                   # 조건에 맞게 나머지 구역을 배치
                            population[0] += area[r][c]
                        
                        elif 0 <= r <= x + d2 and y < c < N:
                            population[1] += area[r][c]
                        
                        elif x + d1 <= r < N and 0 <= c < y - d1 + d2:
                            population[2] += area[r][c]

                        else:                        
                            population[3] += area[r][c]
                
                dif = max(population) - min(population)                                         # 인구를 구했다면 최대값과 최소값의 차이를 구해서
                answer = min(answer, dif)                                                       # 결과를 갱신

print(answer)
