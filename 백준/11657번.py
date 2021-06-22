n, m = map(int, input().split())
INF = int(1e9)

edges = [] # 모든 간선에 대한 정보
dist = [INF] * (n+1) # 최단거리 리스트

# 그래프 생성
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

# 벨만-포드 알고리즘
def bf(start):
    # 시작 노드 0으로 초기화
    dist[start] = 0
    # 정점 수만큼 반복
    for i in range(n):
        # 반복마다 모든 정점 확인
        for j in range(m):
            node = edges[j][0] # 현재 노드
            next_node = edges[j][1] # 연결된 노드
            cost = edges[j][2] # 걸리는 시간

            # 현재 노드에 방문한 적 있음 + 지금 간선으로 가는 최단거리가 연결된 노드의 최단거리보다 작음
            if dist[node] != INF and dist[next_node] > dist[node] + cost:
                # 최단거리 업데이트
                dist[next_node] = dist[node] + cost
                # n번째 노드까지 왔다면 - 사이클 존재
                if i == n-1:
                    return True
    return False

negative_cycle = bf(1)

if negative_cycle:
    print(-1)
else:
    # 1번노드로 가는 최단거리는 출력 X
    for i in range(2, n+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])
