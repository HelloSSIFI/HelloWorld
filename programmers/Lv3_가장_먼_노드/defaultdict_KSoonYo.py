# defaultdict 초기값 설정 방법
# 임의의 key값에 대해 초기 value를 설정해주는 방법
# 딕셔너리(와 유사한 자료구조)에 없는 key값으로도 default value를 출력할 수 있다.

from collections import defaultdict


a = defaultdict(lambda : ['a', 'b'])
print(a[1]) # ['a', 'b']
print(a['a'])

b = defaultdict(list)
print(b['a']) # []

x = defaultdict(int)
print(x['anykey']) # 0

