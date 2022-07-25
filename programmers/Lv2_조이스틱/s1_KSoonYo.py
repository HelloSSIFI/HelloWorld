# fail

minV = 987654321
def change_count(alphas, char):
    loc = alphas.index(char)
    up = loc
    down = 26 - loc
    
    result = 0
    if up <= down:
        result = up
    else:
        result = down
    return result

def move(idx, cnt, name, temp, alphas):
    global minV
    if temp == name:
        minV = min(cnt - 1, minV)
        return

    if idx >= len(name):
        return

    if temp[idx] != name[idx]:
        cnt += change_count(alphas, name[idx])
        temp2 = ''
        for i in range(len(name)):
            if idx >= 0:
                if i == idx:
                    temp2 += name[i]
                    continue
                temp2 += temp[i]

            elif idx < 0:
                if -(i + 1) == idx:
                    temp2 = name[-(i + 1)] + temp2
                    continue
                temp2 = temp[-(i + 1)] + temp2
        
        temp = temp2

        move(idx + 1, cnt + 1, name, temp, alphas)
        move(idx - 1, cnt + 1, name, temp, alphas) 

def solution(name):
    answer = 0    
    alpha_list = [chr(i) for i in range(65, 91)]
    init_name = 'A' * len(name)
    move(0, 0, name, init_name, alpha_list)
    answer = minV
    return answer


# print(solution("JAZ"))
# print(solution("JAN"))
# print(solution("JEROEN"))


a = 'abcdefg'
print(a[-1:])
