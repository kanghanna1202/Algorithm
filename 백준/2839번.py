import sys


def solution(n):
    dp = [0, 5000, 5000, 1, 5000, 1]

    for i in range(6, n+1):
        dp.append(min(dp[i-3], dp[i-5]) + 1)

    if dp[n] >= 5000:
        return -1
    
    return dp[n]


n = int(sys.stdin.readline())

print(solution(n))
