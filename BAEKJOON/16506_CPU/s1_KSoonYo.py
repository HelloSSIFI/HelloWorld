import sys
input = sys.stdin.readline

table = {
    'ADD' : '0000', 'SUB' : '0001', 'MOV' : '0010',
    'AND' : '0011', 'OR' : '0100', 'NOT' : '0101',
    'MULT' : '0110', 'LSFTL' : '0111', 'LSFTR' : '1000',
    'ASFTR' : '1001', 'RL' : '1010', 'RR' : '1011'
}

final_table = {

}

for key in table.keys():
    final_table[key] = table[key]
    if key != 'NOT':
        final_table[key + 'C'] = table[key]    


TC = int(input().strip())
for _ in range(TC):
    opcode, rD, rA, num = input().strip().split()
    first = final_table[opcode]
    if opcode == 'NOT' or opcode[-1] != 'C':
        first += '00'
    else:
        first += '10'

    rD_bin = format(int(rD), 'b')
    second = '0' * (3 - len(rD_bin)) + rD_bin

    if rA == '0':
        third = '000'
    else:
        rA_bin = format(int(rA), 'b')
        third = '0' * (3 - len(rA_bin)) + rA_bin
    
    if first[4] == '0':
        rB_bin = format(int(num), 'b') 
        fourth = '0' * (3 - len(rB_bin)) + rB_bin + '0'
    else:
        C_bin = format(int(num), 'b')
        fourth = '0' * (4 - len(C_bin)) + C_bin
    
    print(first + second + third + fourth)

    