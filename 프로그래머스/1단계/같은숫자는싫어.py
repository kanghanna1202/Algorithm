def solution():
    arr = [4, 4, 4, 3, 3]
    result = [-1]
    idx = 0

    for i in arr:
        if result[idx] != i:
            idx += 1
            result.append(i)

    answer = result[1:]
    print(answer)


solution()
