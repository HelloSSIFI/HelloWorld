
N = int(input())
MAX_LENGTH = 10                                     # 9876543210
numbers = []

def combination(n, i = 0, temp = ''):
    '''
    n : 최대 자릿수
    i : 현재 자릿수
    temp: 현재 숫자
    '''
    if i == n:
        numbers.append(int(temp))
        return
    
    for k in range(0, 10):
        if n > 1 and i == 0 and k == 0:             # 최대 자릿수가 1보다 클 때, 맨 앞 숫자로 0이 오는 것 방지
            continue

        if not temp or int(temp[-1]) > k:
            combination(n, i + 1, temp + str(k))
        else:
            return
for i in range(1, MAX_LENGTH + 1):                  # 자릿수 ( 1 자리수 ~ 최대 자리수)
    combination(i)

if len(numbers) > N:                            
    ans = sorted(numbers)[N]
else:                                               # 조합의 길이보다 N이 크거나 같으면 수를 출력할 수 없다.
    ans = -1

print(ans)
