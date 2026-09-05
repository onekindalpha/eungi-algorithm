from collections import deque

def solution(maps):
  n = len(maps)
  m = len(maps[0])
  # map 은 1-index이고 처음칸은 그냥 0으로 채우면 되는건가. 
  # 각 칸에 대해 방문했는지를 표시해야 
  visited = [[False] * (m+1) for _ in range(n+1)]
  # distance 배열을 만들기로 함. 해당 위치까지 가는데 걸리는 거리. (한칸씩만 더하면 되니까)
  distance = [[0] * (m+1) for _ in range(n+1)]
  # 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수 최소값을 구해라. 
  # 동서남북 방향으로 한 칸 씩 이동
  dr = [0, 0, 1, -1]
  dc = [1, -1, 0, 0]
  # 파이썬에서 queue를 사용하려면 deque를 보통 사용하고 문서 대기열을 생성함. 
  queue = deque()
  # 처음 시작 위치는 (1, 1)이고 도착위치는 (n, m)임
  # 파이썬 상으로는 (0, 0) 이고 distance = 1 임. 처음 위치까지 가는데 1임. 
  start = (0, 0, 1)
  # row, col , distance 임
  queue.append(start)
  visited[0][0] = True
  # 방문을 할때는 queue로 함. bfs는 보통 queue를 이용해서 푸니까.  
  while queue:
  # bfs는 인접하고 방문하지 않은 노드들을 레벨 오더 순으로 방문을 하기 때문에
  # queue 에 append를 하고. 꺼낼 때는 popleft를 함.
  # 파이썬 인덱스는 n-1이랑 m-1로 함.  
    c_r, c_c, distance = queue.popleft()
    if c_r == n-1 and c_c == m-1:
        return distance
    # 그리고 상하좌우 중에 갈만한 칸이 있는지 봐야함
    for i in range(4):
      n_r = c_r + dr[i]
      n_c = c_c + dc[i]
      # 1. 만약 방문했으면 가지 않음.  
      if visited[n_r][n_c] == True:
        continue
      # 2. 만약 게임 진영 밖이면 가지 않음. 
      if n_r < 0 or n_r >= n or n_c < 0 or n_c >= m:
        continue
      # 3. 만약 벽이 있는 자리이면 가지 않음. 
      if maps[n_r][n_c] == 0:
        continue
      # 여기까지 오면 nr_nc를 어펜드를 함. 
      queue.append((n_r, n_c, distance+1))
      # 새롭게 추가한 노드에 대해서 방문처리를 함. 
      visited[n_r][n_c] = True
      # 지나가야 하는 칸의 개수의 최솟값
      # 최단거리 물어보는 것 같고 모든 칸은 그냥 1로 동일한 것 같음.     
  # 만약에 구하지 못하면 -1을 반환함. 
  return -1
# 11
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
# -1
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
