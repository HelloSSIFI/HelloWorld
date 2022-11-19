
def solution(elements):
    answer = 0
    numbers = set()
    
    double_elements = elements * 2
    
    for sub_length in range(len(elements)):
        for s in range(len(elements)):
            temp = double_elements[s: s + sub_length + 1]
            numbers.add(sum(temp))
        
    answer = len(numbers)
    return answer
