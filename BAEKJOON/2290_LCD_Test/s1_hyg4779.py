s, n = input().split()
s = int(s)
m = len(n)
f_line = [
    ' '*(s+2),              # 1, 4
    ' '+'-'*s+' '           # 나머지
]

m_line = [
    ' '*(s+2),              # 1, 7, 0
    ' '+'-'*s+' ',          # 나머지
]

l_line = [
    ' '*(s+2),              # 1, 4, 7
    ' '+'-'*s+' '           # 나머지
]

f_body = [
    ' '*(s+1)+'|',          # 1, 2, 3, 7
    '|'+' '*s+'|',          # 4, 8, 9, 0
    '|'+' '*(s+1)           # 5, 6
]

s_body = [
    ' '*(s+1)+'|',          # 1, 3, 4, 5, 6, 7, 9
    '|'+' '*s+'|',          # 6, 8, 0
    '|'+' '*(s+1)           # 2
]

for a in range(m):
    print(f_line[0], end=' ') if n[a] in '14' else print(f_line[1], end=' ')
print()

for _ in range(s):
    for b in range(m):
        if n[b] in '1237':
            print(f_body[0], end=' ')
        elif n[b] in '4890':
            print(f_body[1], end=' ')
        else:
            print(f_body[2], end=' ')
    print()

for c in range(m):
    print(m_line[0], end=' ') if n[c] in '170' else print(m_line[1], end=' ')
print()

for _ in range(s):
    for d in range(m):
        if n[d] in '680':
            print(f_body[1], end=' ')
        elif n[d] == '2':
            print(f_body[2], end=' ')
        else:
            print(f_body[0], end=' ')
    print()


for e in range(m):
    print(l_line[0], end=' ') if n[e] in '147' else print(l_line[1], end=' ')
print()