S = input()
P = input()

def make_table(pattern):
    table = [0] * len(pattern)
    j = 0
    for i in range(1, len(table)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return table

def kmp(parent, pattern):
    table = make_table(pattern)
    j = 0

    for i in range(len(parent)):
        while j > 0 and parent[i] != pattern[j]:
            j = table[j-1]
        if parent[i] == pattern[j]:
            if j == len(pattern) - 1:
                return 1
            else:
                j += 1
    return 0

print(kmp(S, P))