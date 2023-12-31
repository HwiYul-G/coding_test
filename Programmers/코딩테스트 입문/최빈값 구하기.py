def solution(array):
    answer = 0
    dic = {}
    for i in array:
        if(i in dic):
            dic[i] += 1
        else:
            dic[i] = 1
    
    max_val = max(dic.values())
    for key in dic.keys():
        if(dic[key] == max_val):
            answer = key
            break

    if list(dic.values()).count(max_val) > 1:
        answer = -1

    return answer