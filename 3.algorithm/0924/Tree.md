# [🌴](https://apps.timwhitlock.info/emoji/tables/unicode#emoji-modal)Tree



> 트리 형태 중 루트에 저장된 값과 n.2번 노드에 저장된 값을 출력해보는 문제

```python
def f(n, N):
    global val
    if n <= N:
        f(2*n, N)
        arr[n] = val
        val += 1
        f(2*n+1, N)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0] * (N+1)
    val = 1
    f(1, N)
    print(f'#{tc} {arr[1]} {arr[N//2]}')
```

- 중위 탐색의 순서대로 노드에 값을 저장해주면 된다
- 루트는 무조건 1번이란 가정하에 가장 왼쪽 리프노드부터 숫자를 넣어주는 알고리즘



> 완전 이진트리 형태 중 부모노드가 자식노드보다 클경우 만족할때까지 부모노드와 값을 바꾸는 문제

```python
def f(n,arr):
    if n//2 == 0:
        return
    else:
        if arr[n//2] > arr[n]:
            arr[n//2], arr[n] = arr[n], arr[n//2]
            f(n//2,arr)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    base = list(map(int, input().split()))
    node_list = [0] + base
    for i in range(1,N+1):
        f(i, node_list)
    total = 0
    tmp = N
    while tmp != 0:
        tmp = tmp//2
        total += node_list[tmp]
    print(f'#{tc} {total}')
```

- 매 노드와 그 값을 넣어주면서 definition을 적용시켜줘서 각각의 조상노드에 다 적용을 시켜준다
- 이후에 N노드의 조상노드의 값들의 합을 구해주는 문제
