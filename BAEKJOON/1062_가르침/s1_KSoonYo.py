# 시간 초과 fail

N, K = map(int, input().split())

characters = ['a', 'n', 't', 'c', 'i']       # 접두어, 접미어에 포함되는 글자
K -= len(characters)
letters = []

def teach(candidates, K):
    global maxV
    if K == 0:
        # 글자를 K개 모두 가르쳤다면 주어진 N개 단어에서 읽을 수 있는 단어 count
        maxV = max(maxV, readable())
        return

    
    # 후보군의 글자를 하나씩 가르친다고 가정
    for letter_idx in range(len(candidates)):
        if candidates[letter_idx] in characters:
            continue

        characters.append(candidates[letter_idx])

        # k-1개 이내로 가르칠 수 있는 다음 글자를 가르치러감
        teach(candidates, K - 1)

        # 가르쳤다고 가정한 단어를 꺼내고 다음 글자를 가르친다고 가정
        characters.pop()    

def readable():
    cnt = 0
    for letter in letters:
        flag = False
        for character in letter:
            if character not in characters:
                flag = True
                break
        if not flag:
            cnt += 1

    return cnt

if K <= 0:
    print(0)
else:
    for _ in range(N):
        word = input()
        word = word.strip('anta')             # 접두어 제거
        letter = word.strip('tica')           # 접미어 제거
        letter = ''.join(list(set(letter)))   # 중복 글자 제거
        letters.append(letter)
    maxV = 0
    candidates = ''.join(letters)
    teach(candidates, K)
    print(maxV)
