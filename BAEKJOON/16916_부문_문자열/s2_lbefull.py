S = input()
P = input()

sub = [0] * len(P)
j = 0
for i in range(1, len(P)):              # 찾고자하는 단어를 0 ~ i 로 쪼개서 반복
    while j > 0 and P[i] != P[j]:       # 접두어와 접미어가 같은 최대 길이를 구함
        j = sub[j - 1]
    
    if P[i] == P[j]:
        j += 1
        sub[i] = j

j = 0
for i in range(len(S)):                 # 전체 문자열 순회
    while j > 0 and S[i] != P[j]:       # j가 0이 아니고 현재 확인중인 S문자와 P문자가 다른 동안 반복
        j = sub[j - 1]                  # sub에 저장된 길이로 인덱스를 바꿔줌
    
    if S[i] == P[j]:                    # 확인중인 두 문자가 같다면
        if j == len(P) - 1:             # 현재 P의 마지막 문자를 확인하였으면 해당 단어를 찾은것이므로
            print(1)                    # 1을 출력 후 반복 종료
            break

        j += 1                          # P의 마지막 문자가 아니라면 j를 1증가 후 다음 반복

else:                                   # S 문자열을 순회하는 동안 break를 만나지 못했다면 P 문자열이 없다는 뜻이므로
    print(0)                            # 0 출력
