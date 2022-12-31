def solution(files):
    result = []
    for file in files:
        head = ''
        number = ''
        idx = 0

        # head 구하기
        for i in range(len(file)):
            if file[i].isdigit():
                idx = i
                break
            head += file[i]

        # number 구하기
        for i in range(idx, len(file)):
            if not file[i].isdigit() or len(number) == 5:
                idx = i
                break
            number += file[i]

        result.append([head, number, file[idx:], file])

    result.sort(key=lambda x: (x[0].lower(), int(x[1])))    # head 소문자로 모두 변환 후 정렬, number 변환 후 정렬

    answer = [res[3] for res in result]

    return answer