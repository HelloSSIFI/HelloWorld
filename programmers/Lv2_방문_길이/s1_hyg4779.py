def solution(dirs):

    move = {
        'U': (0, -1),
        'D': (0, 1),
        'L': (-1, 0),
        'R': (1, 0)
    }

    x, y = 0, 0
    route = set()
    for d in dirs:

        r, c = move[d]

        if -5 <= x + r <= 5 and -5 <= y + c <= 5:
            if ((x, y), (x+r,  y+c)) not in route and ((x+r,  y+c), (x, y)) not in route:
                route.add(((x, y), (x+r,  y+c)))
            x += r
            y += c

    return len(route)

print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))