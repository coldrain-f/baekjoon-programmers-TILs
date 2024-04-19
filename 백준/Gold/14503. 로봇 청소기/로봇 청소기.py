def solution(x, y, d, board):  
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    answer = 0
    
    while True:
      if board[x][y] == 0:
        board[x][y] = -1
        answer += 1
      
      cleaned = True
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 청소할 곳이 있음
        if board[nx][ny] == 0: 
          cleaned = False
      
      if cleaned:
        nx = x - dx[d]
        ny = y - dy[d]
        if board[nx][ny] == 1:
          return answer
        x = nx
        y = ny
      else:
        d = (d + 3) % 4
        nx = x + dx[d]
        ny = y + dy[d]
        if board[nx][ny] == 0:
          x = nx
          y = ny

    return answer
   

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
print(solution(r, c, d, arr))