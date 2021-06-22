# 푸는중

import math

def solution(progresses, speeds):
    answer = []
    queue = []
    
    for i in range(len(progresses)):
        x = math.ceil((100-progresses[i])/speeds[i])
        queue.append(x)
    
    cnt = 0
    while queue:  # [5, 10, 1, 1, 20, 1] -> [5, -4, -4, 15, -4]
        x = queue.pop(0)
        cnt += 1
        for i in queue:
            i -= x
        for i in queue:
            if i <= 0:
                queue.pop(0)
                cnt += 1
            else:
                break
        answer.append(cnt)
        cnt = 0

    return answer


print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]	))
