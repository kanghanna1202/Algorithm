# 아직 해결 안함.

def solution(N, number):
    s = set()
    s.add(N)

    if N==number:
        return 1
    
    for i in range(2, 9):
        k = set()
        k.add(N*int('1'*i))
        for j in s:
            k.add(j+N)
            k.add(j-N)
            k.add(j*N)
            k.add(j//N)
        s.update(k)
        if number in s:
            if i > 8:
                return -1
            return i
    return -1


print(solution(5, 31168))
