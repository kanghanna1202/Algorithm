# M과 N이 주어질 때 M이상 N이하의 자연수 중 완전제곱수인 것을 모두 골라 그 합을 구하고 그 중 최솟값을 찾는 프로그램을 작성하시오.
# 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 완전제곱수는 64, 81, 100 이렇게 총 3개가 있으므로 그 합은 245가 되고 이 중 최솟값은 64가 된다.
# M <= N <= 10000
# 1. 모든 완전 제곱수를 구해둔다.
# 2. 범위에 맞는 것만 구한다 -> 어떻게? 제곱근 함수? math.sqrt(60) -> 7.74....이걸 ceil 이용해서 올리면 될듯. 반대는 floor

import sys

import math

# input보다 속도가 빠름
m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

x = math.ceil(math.sqrt(m)) # 60 -> 7.74~ -> 8
y = math.floor(math.sqrt(n)) # 100 -> 10 - 10

if x >= y:
    print(-1)
else:
    cnt = 0
    for i in range(x, y+1):
        cnt += i*i
    print(cnt)
    print(x*x)
