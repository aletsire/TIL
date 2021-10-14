# 최소 신장 트리(MST)

- 그래프에서 최소 비용 문제

  - 모든 정점을 연결하는 간선들의 가중치의 합이 최소가 되는 트리

  - 두 정점 사이의 최소 비용의 경로 찾기

- 신장 트리

  - n개의 정점으로 이루어진 무방향 그래프에서 n개의 정점과 n-1개의 간선으로 이루어진 트리

- 최소 신장 트리(Minimum Spanning Tree)

  - 무방향 가중치 그래프에서 신장 트리를 구성하는 간선들의 가중치의 합이 최소인 신장 트리



### Prim 알고리즘

- 하나의 정점에서 연결된 간선들 중에 하나씩 선택하면서 MST를만들어 가는 방식
  - 임의 정점을 하나 선택해서 시작
  - 선택한 정점과 인접하는 정점들 중의 최소 비용의 간선이 존재하는 정점을 선택
  - 모든 정점이 선택될 때까지 1, 2 과정을 반복



### 예시 코드


```python
def prim1(r, V):
    MST = [0]*(V+1)     # MST 포함여부
    key = [10000]*(V+1) # 가중치의 최대값 이상으로 초기화. key[v]는 v가 MST에 속한 정점과 연결될 때의 가중치
    key[r] = 0          # 시작정점의 key
    for _ in range(V):  # V+1개의 정점 중 V개를 선택
        # MST에 포함되지 않은 정점 중(MST[u]==0), key가 최소인 u 찾기
        u = 0
        minV = 10000
        for i in range(V+1):
            if MST[i]==0 and key[i]<minV:
                u = i
                minV = key[i]
        MST[u] = 1                  # 정점 u를 MST에 추가
        # u에 인접인 v에 대해, MST에 포함되지 않은 정점이면
        for v in range(V+1):
            if MST[v]==0 and adjM[u][v]>0:
                key[v] = min(key[v], adjM[u][v])     # u를 통해 MST에 포함되는 비용과 기존 비용을 비교, 갱신
    return sum(key)         # MST 가중치의 합

def prim2(r, V):
    MST = [0]*(V+1)     # MST 포함여부
    MST[r] = 1
    s = 0
    for _ in range(V):
        u = 0
        minV = 10000
        for i in range(V+1):    # MST에 포함된 정점i와 인접한 정점j 중 MST에 포함되지 않고 가중치가 최소인 정점 u찾기
            if MST[i]==1:
                for j in range(V+1):
                    if adjM[i][j]>0 and MST[j]==0 and minV>adjM[i][j]:
                        u = j
                        minV = adjM[i][j]
        s += minV
        MST[u] = 1
    return s

V, E = map(int, input().split())
adjM = [[0]*(V+1) for _ in range(V+1)]
adjL = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adjM[u][v] = w
    adjM[v][u] = w  # 가중치가 있는 무방향 그래프
    adjL[u].append((v, w))
    adjL[v].append((u, w))
print(adjM)
print(adjL)
#print(prim1(0, V))
print(prim2(0, V))
```

