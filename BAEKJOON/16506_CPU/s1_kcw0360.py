N = int(input())

opcode_dict = {'ADD': '000000', 'ADDC': '000010', 'SUB': '000100', 'SUBC': '000110', 'MOV': '001000', 'MOVC': '001010',
               'AND': '001100', 'ANDC': '001110', 'OR': '010000', 'ORC': '010010', 'NOT': '010100',
               'MULT': '011000', 'MULTC': '011010', 'LSFTL': '011100', 'LSFTLC': '011110', 'LSFTR': '100000', 'LSFTRC': '100010',
               'ASFTR': '100100', 'ASFTRC': '100110', 'RL': '101000', 'RLC': '101010', 'RR': '101100', 'RRC': '101110'}
r_dict = {'0': '000', '1': '001', '2': '010', '3': '011', '4': '100', '5': '101', '6': '110', '7': '111'}
rc_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000',
            '9': '1001', '10': '1010', '11': '1011', '12': '1100', '13': '1101', '14': '1110', '15': '1111'}

answer = []
for _ in range(N):
    op, rd, ra, r = input().split()
    if op[-1] == 'C':
        temp = opcode_dict[op] + r_dict[rd] + r_dict[ra] + rc_dict[r]
    else:
        temp = opcode_dict[op] + r_dict[rd] + r_dict[ra] + r_dict[r] + '0'

    answer.append('{}\n'.format(temp))

print(''.join(answer))