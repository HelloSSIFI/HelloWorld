import sys
input = sys.stdin.readline


cod = {'ADD': 0, 'SUB': 1, 'MOV': 2, 'AND': 3, 'OR': 4, 'NOT': 5, 'MULT': 6, 'LSFTL': 7, 'LSFTR': 8, 'ASFTR': 9, 'RL': 10, 'RR': 11}
answers = []
for _ in range(int(input())):
    com, rD, rA, rB = map(lambda x: int(x) if x.isdigit() else x, input().split())

    if com in cod:                                                      # 명령어가 cod 딕셔너리 안에 있을경우
        op = cod[com]                                                   # op에 해당 숫자를 저장
        four = 0                                                        # 이 경우 4번 bit는 0
    else:                                                               # 딕셔너리 안에 없을경우
        op = cod[com[:-1]]                                              # 끝에 C가 붙은 명령이므로 C를 제거한 명령을 cod에서 찾아 저장
        four = 1                                                        # 이 경우 4번 bit는 1
    
    answer = (op << 12) + (four << 11) + (rD << 7) + (rA << 4)          # 각각 명령어와 레지스터의 위치에 맞게 bit shift
    if four:                                                            # 4번 bit가 있을경우
        answer += rB                                                    # 3자리 모두 사용하므로 그대로 더해줌
    else:                                                               # 4번 bit가 0일 경우
        answer += rB << 1                                               # 마지막자리를 사용하지 않으므로 왼쪽으로 1칸 옮겨줌
    
    answers.append(bin(answer)[2:].zfill(16))                           # 16자리에 맞게 0을 채워줌

print('\n'.join(answers))
