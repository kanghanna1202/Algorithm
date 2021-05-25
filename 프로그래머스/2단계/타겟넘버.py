def solution(numbers, target):
    answer = dfs(numbers, target, 0)
    return answer

def dfs(numbers, target, idx):
    answer = 0

    # 현재 인덱스가 마지막일 경우
    if idx == len(numbers):
        # 다 더해야 타겟 값이 나오는 경우
        if sum(numbers) == target:
            return 1
        else:
            return 0
    else:
        # 인덱스 값을 더하고 dfs
        answer += dfs(numbers, target, idx + 1)
        # 음수 값으로 바꾼 뒤 dfs
        numbers[idx] *= -1
        answer += dfs(numbers, target, idx + 1)
    return answer


print(solution([1, 1, 1, 1, 1], 3))
