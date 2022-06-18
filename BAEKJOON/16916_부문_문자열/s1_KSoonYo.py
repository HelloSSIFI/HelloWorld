# 10% fail

import sys
from collections import deque

input = sys.stdin.readline

string = input().strip()
queue = deque(string)

pattern = input().strip()
pointer = 0

while queue:
    char = queue.popleft()
    if char == pattern[pointer]:
        pointer += 1

        if pointer == len(pattern):
            print(1)
            exit()
    
    else:
        pointer = 0
print(0)