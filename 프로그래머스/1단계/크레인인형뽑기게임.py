def solution():
    board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
    moves = [1, 5, 3, 5, 1, 2, 1, 4]
    solution_list = [0]
    idx = 1
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                if solution_list[idx-1] == board[j][i-1]:
                    solution_list.pop(idx-1)
                    idx -= 1
                    answer += 2
                else:
                    solution_list.append(board[j][i-1])
                    idx += 1

                board[j][i-1] = 0
                print(solution_list)
                break

    print(answer)


solution()
