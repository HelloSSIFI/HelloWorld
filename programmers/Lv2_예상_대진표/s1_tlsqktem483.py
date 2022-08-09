def solution(N, A, B):
    A -= 1
    B -= 1
    ans = 1

    def battle(a, b):
        nonlocal ans

        if a == b:
            return
        else:
            ans += 1
            battle(a//2, b//2)

    battle(A, B)
    return ans - 1


print(solution(8, 4, 7))