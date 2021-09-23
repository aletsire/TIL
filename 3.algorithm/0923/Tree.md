# [🌴](https://apps.timwhitlock.info/emoji/tables/unicode#emoji-modal)Tree

- 트리는 정점(node)와 간선(edge)를 이용하여 데이터의 배치 형태를 추상화한 자료구조
- Root노드: 트리의 가장 윗 부분에 있는 노드
- Leaf노드: 자식 노드를 갖고 있지 않는 노드



## [🌵](https://apps.timwhitlock.info/emoji/tables/unicode#emoji-modal)[🌵](https://apps.timwhitlock.info/emoji/tables/unicode#emoji-modal)이진 트리

- 하나의 노드에 2개의 서브 트리가 있는 노드(오직 2개만!)
- 포화 이진트리: 모든 level과 칸이 노드로 가득 차있는 이진트리
- 완전 이진트리: 모든 칸이 노드로 가득 차있지는 않지만 순서대로 노드가 들어있는 이진트리



> 트리 형태 중 중위 순회를 이용해서 N 노드의 자식 노드의 수를 구해보는 문제

```python
def f(n):
    global cnt
    if n:
        f(ch1[n])
        cnt += 1
        f(ch2[n])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    V = E + 1
    cnt = 0
    ch1 = [0] * (V+1) # 부모를 인덱스로 자식번호 저장
    ch2 = [0] * (V + 1)
    arr = list(map(int, input().split()))
    for i in range(E):
        n1, n2 = arr[i*2], arr[i*2 + 1]
        if ch1[n1] == 0:
            ch1[n1] = n2
        else:
            ch2[n1] = n2
    f(N)
    print(f'{tc} {cnt}')
```

- 문제에서 한개의 부모 노드에 최대 두개의 자식 노드가 있다고 가정했으니 두개의 채널을 가정해주고 각 채널에 부모 인덱스로 자식 노드 번호를 저장한다
- 자식 노드가 없을 경우 카운트를 하지 않고 각 있을 경우마다 카운트를 해준다.
