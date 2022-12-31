def solution(msg):
    answer = []
    my_dict = {chr(i): i-64 for i in range(65, 91)}
    i, j, k = 0, 1, 27

    while i < len(msg):

        while i + j <= len(msg):
            w = msg[i:i + j]

            if my_dict.get(w, 0):
                j += 1

            else:
                my_dict[w] = k
                k += 1
                break

        answer.append(my_dict[msg[i:i+j-1]])

        i = i+j-1
        j = 1

    return answer