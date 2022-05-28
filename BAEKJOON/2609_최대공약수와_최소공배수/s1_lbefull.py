A, B = map(int, input().split())

greatest_deno = 0                   # 최대 공약수
least_multi = 0                     # 최소 공배수

for i in range(A, 0, -1):           # 최대 공약수는 공약수중 가장 큰 수 이므로 큰 수부터 탐색
    if not A % i and not B % i:     # A와 B가 각각 i로 나누었을 때 나머지가 0 이면
        greatest_deno = i           # 최대 공약수로 i를 지정하고 break
        break

for i in range(1, B + 1):           # 최소 공배수는 A 혹은 B와 같은값부터 A * B 사이에 있고 A와 B의 배수이므로 해당 범위 탐색
    if not (A * i) % B:             # A와 B로 나누었을 때 나머지가 0이면
        least_multi = A * i         # 최소 공배수로 A * i를 지정하고 break
        break

print(greatest_deno)
print(least_multi)
