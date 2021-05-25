def solution(prices):
    answer = [len(prices)-i-1 for i in range(len(prices))]
    stack = [0]

    for i in range(1, len(prices)-1):
        while stack:
            idx = stack[-1]
            if prices[i] < prices[idx]:
                answer[idx] = i - idx
                stack.pop()
            else:
                break

        stack.append(i)

    return answer


print(solution([1, 2, 3, 2, 3]))


# 스택 사용 X
# def solution(prices):
#     answer = []
#
#     for i in range(len(prices)):
#         cnt = 0
#         for j in range(i+1, len(prices)):
#             cnt += 1
#             if prices[i] > prices[j]:
#                 break
#         answer.append(cnt)
#
#     return answer
