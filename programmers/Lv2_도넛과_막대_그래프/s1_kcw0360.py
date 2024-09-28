from collections import defaultdict

def solution(edges):
    answer = [0, 0, 0, 0]

    graph = defaultdict(lambda: [0, 0])

    for edge in edges:
        a, b = edge
        graph[a][0] += 1
        graph[b][1] += 1

    for key, val in graph.items():
        out_dir, in_dir = val

        if out_dir == 0:
            answer[2] += 1
        elif out_dir == 2:
            if in_dir > 0:
                answer[3] += 1
            else:
                answer[0] = key
                root = key
        elif out_dir > 2:
            answer[0] = key
            root = key

    answer[1] = graph[root][0] - answer[2] - answer[3]

    return answer