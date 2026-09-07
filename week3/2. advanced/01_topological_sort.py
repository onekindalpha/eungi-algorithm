"""
[위상 정렬 - Topological Sort]

문제 설명:
- 방향 그래프에서 순서를 정합니다.
- 선행 작업이 먼저 오도록 정렬합니다.
- 예: 과목 선수과목, 작업 순서

입력:
- graph: 방향 그래프
- vertices: 정점 개수

출력:
- 위상 정렬 순서

예제:
과목:
0(기초) → 1(중급) → 3(고급)
0(기초) → 2(응용)

위상 정렬: [0, 1, 2, 3] 또는 [0, 2, 1, 3]

힌트:
- 진입 차수(in-degree) 사용
- 진입 차수가 0인 정점부터 시작
- 큐 사용
"""

from collections import deque

def topological_sort(vertices, edges):
    """
    위상 정렬 (Kahn's Algorithm)
    
    Args:
        vertices: 정점 개수
        edges: (출발, 도착) 간선 리스트
    
    Returns:
        위상 정렬 순서
    """
    # TODO: 그래프와 진입 차수 초기화
    n = vertices
    graph = {}
    result = []
    # 진입차수를 저장할 곳임. 
    indegree = [0] * n 
    # 그래프를 초기화함. 
    for vertice in range(vertices):
        graph[vertice] = []
    # 간선에 대한 그래프를 만들고, v에 대해서는 진입차수를 하나 추가함. 
    # 그냥 v라고만 하는 이유는 indegree가 0부터 시작함. 
    for u, v in edges:
        graph[u].append(v)
        indegree[v] +=1
    # 문서 대기열을 만들고
    queue=deque()
    # 방문한 노드는 더이상 방문하지 않기로 함. 
    visited = [False] * n
    # 각 노드들에 대해 
    for vertice in range(vertices):
        # 진입차수가 0인 정점들을 큐에 추가하고. 
        if indegree[vertice] ==0:
            queue.append(vertice)
            visited[vertice] = True
            # TODO: 진입 차수가 0인 정점들을 큐에 추가
    # TODO: 큐가 빌 때까지 반복
    while queue:
        ## 큐에서 정점 꺼내기
        c_node = queue.popleft()
        # pop을 한 순서가 위상정렬임. 
        result.append(c_node)
        ## 아 근데 인접한 정점이네 - 인ㅈ버한 노드들에 대해서만. 
        for next_node in graph[c_node]:
        ## 인접한 정점들의 진입 차수 감소
        ## 인접한 정점 노드의 숫자가 나오겠지
            indegree[next_node] -= 1
        # 마만약 진입차수가 0이 되면 푸시를 함
        # 남은 것에 대해 돌아야 하나......
        # 큐에서 하나 팝했으면 팝한 만큼 range를 주라고 한 것 같은데 . 
        for i in range(n):
            if indegree[i] == 0 and not visited[i]:
                queue.append(i)
                visited[i] = True
    return result

# 테스트 케이스
if __name__ == "__main__":
    # 과목 선수과목 예제
    vertices = 4
    edges = [
        (0, 1),  # 0 → 1
        (0, 2),  # 0 → 2
        (1, 3),  # 1 → 3
    ]
    
    print("=== 위상 정렬 ===")
    print("과목 관계:")
    print("  0(기초) → 1(중급) → 3(고급)")
    print("  0(기초) → 2(응용)")
    print()
    
    result = topological_sort(vertices, edges)
    print(f"수강 순서: {result}")
