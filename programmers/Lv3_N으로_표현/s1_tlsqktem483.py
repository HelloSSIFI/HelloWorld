def solution(N, number):
    n_list = []

    if N == number:
        return 1
    for i in range(1, 9):
        temp = set()
        temp.add(int(str(N)*i))
        for j in range(0, i-1):
            for n1 in n_list[j]:
                for n2 in n_list[-j-1]:
                    temp.add(n1 + n2)
                    temp.add(n1 - n2)
                    temp.add(n1 * n2)
                    if n2 != 0:
                        temp.add(n1 // n2)

        if number in temp:
            return i
        n_list.append(temp)
    return -1