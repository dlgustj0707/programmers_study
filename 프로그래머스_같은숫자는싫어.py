def solution(arr):
    answer = []
    answer.append(arr[0])
    i = 1
    while i < len(arr):
        answer.append(arr[i]) 
        j = len(answer) - 1 #answer의 마지막 원소가 몇번째인지를 나타냄
        if answer[j-1] == answer[j]: #끝에 있는 두 원소 비교 
            answer.pop()
        i += 1
    return answer
