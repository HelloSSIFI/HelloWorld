def solution(s):
    words = []
    for word in s.split(' '):
        words.append(word.capitalize())

    return ' '.join(words)
