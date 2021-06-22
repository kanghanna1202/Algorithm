# 수의 범위가 크기 때문에 완전탐색으로 어려움
# 이진탐색 하는 것: 한 명의 심사관에게 얼마의 시간을 주는지
# 총 걸리는 시간의 최선과 최악을 구한 뒤 중간 값으로 완료할 수 있는지 확인
# 한 심사관이 mid의 시간동안 몇 명의 사람을 심사할 수 있는지 확인
# 심사한 사람이 n값보다 많으면 시간을 줄이고, n값보다 적으면 시간을 늘린다.
def solution(n, times):
    # 최악의 시간
    right = max(times) * n
    left = 0

    while left <= right:
        # 심사관에게 주는 시간
        mid = (right + left) // 2

        # 주어진 시간동안 몇 명을 심사했는지
        people = 0
        for i in times:
            # 주어진 시간동안 현재 심사관이 심사할 수 있는 사람 누적하기
            people += mid//i

            # 모든 사람을 심사 가능할 경우
            if people >= n:
                answer = mid
                right = mid - 1
                break
        
        # 모든 사람을 심사할 수 없는 경우
        if people < n:
            left = mid + 1

    return answer


print(solution(6, [7, 10]))
