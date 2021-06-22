from collections import deque

def solution(n, computers):
    # nw의 수, 방문한 노드, 탐색 큐
    answer = 0
    visited = [0] * n
    bfs = deque()

    # 모두 탐색할 때까지 반복
    while 0 in visited:
        # 탐색하지 않은 노드 찾기
        idx = visited.index(0)
        # 탐색 큐에 넣기
        bfs.append(idx)
        visited[idx] = 1

        # 큐가 빌 때까지 반복
        while bfs:
            # 탐색큐의 값을 빼고 방문했다고 체크
            node = bfs.popleft()
            visited[node] = 1

            # 인접노드 방문하기
            for i in range(n):
                if visited[i] == 0 and computers[node][i] == 1:
                    bfs.append(i)
                    visited[i] = 1
            
            # 네트워크 하나 탐색 끝
        answer += 1
    return answer


print(solution(3, [[1, 1, 1], [0, 1, 0], [1, 1, 1]]	))