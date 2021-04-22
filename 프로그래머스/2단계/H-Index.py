def solution():
    citations = [12, 11, 10, 9, 8, 1]
    for i in range(max(citations), 0, -1):
        answer = 0
        for citation in citations:
            if citation >= i:
                answer += 1
            if answer == i:
                return answer


solution()
