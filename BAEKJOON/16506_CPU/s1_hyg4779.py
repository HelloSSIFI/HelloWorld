arr = {
    'ADD': '0000',
    'SUB': '0001',
    'MOV': '0010',
    'AND': '0011',
    'OR': '0100',
    'NOT': '0101',
    'MULT': '0110',
    'LSFTL': '0111',
    'LSFTR': '1000',
    'ASFTR': '1001',
    'RL': '1010',
    'RR': '1011',
}

def change(num:object=str, octor:object=int):
    if num=='0' and octor:
        return '000'
    if num=='0':
        return '0000'

    num = bin(int(num))[2:]
    return '0'*(3-len(num))+num if octor else '0'*(4-len(num))+num

n = int(input())

for i in range(n):
    comm, rD, rA, rB = input().split()
    answer = ''
    C = False

    if comm[-1]=='C':
        answer += arr[comm[:-1]]+'10'
        C = True
    else:
        answer += arr[comm]+'00'

    answer += change(rD, 1) + change(rA, 1)

    print(answer + change(rB, 0) if C else change(rB, 1)+'0')