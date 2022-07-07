from collections import Counter


def solution(str1, str2):
    comb1 = []
    comb2 = []

    for i in range(len(str1)-1):
        c1 = str1[i:i+2]
        if c1.isalpha():
            comb1.append(c1.lower())
    for j in range(len(str2)-1):
        c2 = str2[j:j+2]
        if c2.isalpha():
            comb2.append(c2.lower())

    comb1 = Counter(comb1)
    comb2 = Counter(comb2)
    intersection = sum([min(comb1[c], comb2[c]) for c in comb1 if c in comb2])
    union = sum([c for c in (comb1+comb2).values()]) - intersection
    if not intersection and not union:
        return 65536
    else:
        return int(intersection/union*65536)


print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))