def solution(files):

    sort_dict = dict()

    # HEAD에 따라 분류
    for f in files:
        # 파일의 길이
        n = len(f)
        head, number, tail = '', '', ''
        for i in range(1, n):
            # 숫자가 등장: NUMBER 부분
            if f[i].isdigit():
                j = i + 1
                while j < n:

                    # 숫자가 나온 경우
                    if f[j].isdigit():
                        # NUMBER 최대 범위
                        if j-i > 5:
                            break
                        # 아직 NUMBER
                        else:
                            pass

                    # 숫자가 아닌 경우
                    else:
                        break

                    j += 1

                # NUMBER 범위 끝
                head, number, tail = f[:i], f[i:j], f[j:]
                break

        if sort_dict.get(head.upper(), 0):
            sort_dict[head.upper()].append((head, number, tail))
        else:
            sort_dict[head.upper()] = [(head, number, tail)]

    # NUMBER에 따라 분류
    for k, v in sort_dict.items():
        sort_dict[k] = sorted(v, key=lambda x: int(x[1]))

    result = sorted(list(sort_dict.items()))
    answer = []
    for _, value in result:
        for tmp in value:
            answer.append(''.join(tmp))

    return answer


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))