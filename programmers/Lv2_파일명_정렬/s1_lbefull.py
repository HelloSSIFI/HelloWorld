def solution(files):
    answer = []
    for file in files:
        head = number = tail = ''
        i = 0
        while not file[i].isdigit():                                    # 숫자가 나오기 전까지 문자열을 head에 저장
            i += 1
        head = file[:i]

        j = i
        while j < len(file) and j - i < 5 and file[j].isdigit():        # 연속된 숫자 최대 5단어를 number에 저장
            j += 1
        number = file[i:j]
        tail = file[j:]                                                 # 나머지 남은 문자열을 tail에 저장
        answer.append([head, number, tail])                             # head, number, tail을 순서대로 리스트로 바꿔서 answer에 추가

    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))                # answer의 요소를 head를 대소문자 구분없이 오름차순 정렬, 만약 같다면 number를 오름차순으로 정렬
    answer = [''.join(el) for el in answer]                             # answer의 각 요소인 문자열 리스트를 합쳐서 문자열로 바꿔서 저장
    return answer


# print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
