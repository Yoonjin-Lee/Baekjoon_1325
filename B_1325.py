from collections import deque


def bfs(start, graph):
    queue = deque()
    queue.append(start)
    visited = [False] * (com_n+1)
    count = 1
    while queue:
        v = queue.popleft()
        visited[v] = True
        if graph[v]:
            for i in graph[v]:
                if not visited[i]:
                    count += 1
                    visited[i] = True
                    queue.append(i)
    return count


com_n, nodes = map(int, input().split())

graph = [[] for _ in range(com_n+1)]
for i in range(nodes):
    a, b = map(int, input().split())
    graph[b].append(a)

check = dict()

for i in range(1, com_n+1):
    if graph[i]:
        check[i] = bfs(i, graph)

max_value = max(check.values())
answer = []

for (i, j) in check.items():
    if j == max_value:
        answer.append(i)

for r in answer:
    print(r, end=' ')
