def solution(clothes):
    d = {}
    answer = 1
    
    for i in clothes:
        if i[1] in d:
            d[i[1]] += 1
        else:
            d[i[1]] = 1

    print(d)

    for k, v in d.items():
        answer *= v+1
    
    return answer-1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
