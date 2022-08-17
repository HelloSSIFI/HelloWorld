# 양방향 연결 리스트 이용

def solution(n, k, cmd):
    answer = ['O'] * n
    table = {}
    remove_stack = []
    for i in range(n):
        table[i] = {'prev' : i - 1, 'next' : i + 1, 'value' : i}

    table[0]['prev'] = None
    table[n-1]['next'] = None

    cursor = k
    for c in cmd:
        command = c.split()
        if len(command) == 2:
            direction, dist = command
            dist = int(dist)
            if direction == 'U':
               for _ in range(dist):
                cursor = table[cursor]['prev']
            else:
                for _ in range(dist):
                    cursor = table[cursor]['next']
        else:
            if command[0] == 'C':
                answer[cursor] = 'X'
                remove_stack.append(table[cursor]['value'])
                if table[cursor]['prev'] == None:
                    table[table[cursor]['next']]['prev'] = None
                elif table[cursor]['next'] == None:
                    table[table[cursor]['prev']]['next'] = None     
                else:
                    table[table[cursor]['prev']]['next'] = table[table[cursor]['next']]['value']
                    table[table[cursor]['next']]['prev'] = table[table[cursor]['prev']]['value']
                if table[cursor]['next'] == None:
                    cursor = table[cursor]['prev']
                else:
                    cursor = table[cursor]['next']
            
            else:
                now = remove_stack.pop()
                answer[now] = 'O'
                if table[now]['prev'] == None:
                    table[table[now]['next']]['prev'] = table[now]['value']
                elif table[now]['next'] == None:
                    table[table[now]['prev']]['next'] = table[now]['value']
                else:
                    table[table[now]['prev']]['next'] = table[now]['value']
                    table[table[now]['next']]['prev'] = table[now]['value']
    answer = ''.join(answer)
    return answer


print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
