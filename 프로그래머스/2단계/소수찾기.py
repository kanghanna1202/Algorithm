import math
from itertools import permutations


def solution(numbers):
    answer = []

    lst = [int(x) for x in str(numbers)]

    for i in range(1, len(lst)+1):
        for j in permutations(lst, i):
            res = ''.join(map(str,j))
            if is_prime(int(res)):
                answer.append(int(res))

    answer = list(set(answer))
    return len(answer)

def is_prime(n):
    if n==0 or n==1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        
        return True


print(solution("011"))