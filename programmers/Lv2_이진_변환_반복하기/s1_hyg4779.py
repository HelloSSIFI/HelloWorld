def solution(s):
    time, zero = 0, 0

    while s != "1":
        time += 1
        new = 0
        for i in s:
            if i == '1':
                new += 1
            else:
                zero += 1

        s = bin(new)[2:]

    return [time, zero]
