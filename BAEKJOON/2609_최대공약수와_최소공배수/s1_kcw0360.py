A, B = map(int, input().split())

def search(n):
    temp = []  # 약수 저장

    # 약수 찾기
    for i in range(1, n + 1):
        if n % i == 0:
            temp.append(i)
    return temp

A_list = search(A)
B_list = search(B)

# 최대공약수 찾기
cd = []
for i in A_list:
    if i in B_list:
        cd.append(i)
cd.sort()
gcd = cd[-1]
print(gcd)

# 최소공배수 찾기
lcm = A * B // gcd
print(lcm)
