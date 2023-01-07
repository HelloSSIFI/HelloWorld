def solution(storey):
    answer = 0

    i = 1

    while storey:
        now = round(storey, -i)

        # 반올림 한게 작다 == 5 이하 => 해당 수 만큼 -버튼 클릭
        if storey > now:
            answer += (storey - now)//(10**(i-1))

        # 반올림 한게 크다 == 6 이상 => 자리수 올리는 만큼 + 버튼 클릭ㅇ
        else:
            answer += (now - storey)//(10**(i-1))

        storey = now
        i += 1

    return answer


print(solution(16))
print(solution(2554))
print(solution(5))