s = input()

def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2 + 1):
        result = ''
        target = s[:i]
        count = 1

        for j in range(i, len(s), i):
            current = s[j:j + i]
            if target == current:
                count += 1
            else:
                if count >= 2:
                    result += str(count) + target
                else:
                    result += target
                target = current
                count = 1

        if count >= 2:
            result += str(count) + target
        else:
            result += target

        answer = len(result) if answer > len(result) else answer

    return answer