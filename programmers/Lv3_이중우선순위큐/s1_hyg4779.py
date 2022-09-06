def solution(operations):

    Q = list()

    def q_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        l = [a for a in arr[1:] if a < pivot]
        r = [b for b in arr[1:] if b >= pivot]
        return q_sort(l) + [pivot] + q_sort(r)

    for comm in operations:
        if comm[0] == 'I':
            Q.append(int(comm.split(' ')[1]))
            new = q_sort(Q)
            Q = new

        else:
            if Q:
                if len(comm) > 3:
                    Q.pop(0)
                else:
                    Q.pop()

    return [Q[-1], Q[0]] if Q else [0, 0]