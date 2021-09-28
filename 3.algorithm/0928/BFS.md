# [✈](https://apps.timwhitlock.info/emoji/tables/unicode#emoji-modal)**BFS**

### 문제: N*M의 지도에서 땅으로 표시된 칸들에 물로 표시된 칸의 최소거리를 구하고 그 합을 구한다

> DFS를 이용해서 문제를 풀어보았을 경우

```python
def solution(i, j, arr, c):
    visited[i][j] = 1
    for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
        ni, nj = i + di, j+ dj
        if 0<=ni<N and 0<=nj<M and visited[ni][nj] == 0:
            if arr[ni][nj] != 0:
                c += 1
                if arr[ni][nj] > c:
                    arr[ni][nj] = c
                    solution(ni, nj,arr, c)
                else:
                    solution(ni, nj,arr, c)
                c -= 1
    visited[i][j] = 0


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    tmp = []
    visited=[]
    for i in range(N):
        visited.append([0]*M)
        for j in range(M):
            if arr[i][j] == 'W':
                arr[i][j] = 0
                tmp.append([i, j])
            else:
                arr[i][j] = 987654321

    for a, b in tmp:
        solution(a, b, arr, 0)
    total = 0
    for i in range(N):
        for j in range(M):
            total += arr[i][j]
    print(f'#{tc} {total}')
```

- 주어진 리스트에서 물로 지정된 지점을 찾아내주고 땅 값과 차이를 둔다.
- visited를 지정해줘서 이미 지나온 곳인지를 확인하게 해준다.
- 함수를 4가지 방향을 통해서 각 물의 위치에서 모든 땅과의 거리를 체크를 하면서 최소값일 경우 교체해주는 과정을 진행해 준다.



### 문제점

- DFS의 경우 원하던 결과가 나오지만 속도가 너무 오래걸려 오류가 발생하게 된다.
- 그래서 queue를 쓰는 BFS를 이용해 줘야 한다. 





> BFS를 사용했을 경우

```python
def bfs(N, M):
    front = -1
    rear = -1
    q = [0] * (N*M)
    visited = [[0]*M for _ in range(N)]
    s = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                rear += 1
                q[rear] = (i,j)
                visited[i][j] = 1
                s+= visited[i][j]
    while front != rear:
        front += 1
        i, j = q[front]
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni,nj = i+di, j+dj
            if 0<=ni<N and 0<= nj<M and visited[ni][nj] == 0:
                rear += 1
                q[rear] = (ni,nj)
                visited[ni][nj] = visited[i][j] + 1
                s += visited[ni][nj]

    return s-N*M

T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    arr = [input() for _ in range(N)]
    print(f'#{tc} {bfs(N,M)}')
```
