

a, b = map(int, input().split())

# 유클리드 호제법
num1 = a
num2 = b

while num2 != 0:
    num1, num2 = num2, num1 % num2
    


# GCD(최대 공약수)
GCD = num1

# LCM(최소 공배수)
if a > b:
    a, b = b, a

LCM = a * (b // GCD)

print(GCD)
print(LCM)