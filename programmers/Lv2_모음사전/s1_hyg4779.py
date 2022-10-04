from itertools import product
'''
itertools product: 중복 순열을 만드는 조합형 이터레이터
product(*args[, repeat=1])
args: 조합할 원소들
repeat: 같은 원소의 중복 횟수
'''
aeiou = ['A', 'E', 'I', 'O', 'U']
def solution(word):
    my_dict = []
    for i in range(1, 6):
        arr = product(aeiou, repeat=i)
        for j in arr:
            my_dict.append(''.join(list(j)))

    my_dict.sort()

    return my_dict.index(word)+1