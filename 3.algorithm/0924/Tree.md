# [๐ด](https://apps.timwhitlock.info/emoji/tables/unicode#emoji-modal)Tree



> ํธ๋ฆฌ ํํ ์ค ๋ฃจํธ์ ์ ์ฅ๋ ๊ฐ๊ณผ n.2๋ฒ ๋ธ๋์ ์ ์ฅ๋ ๊ฐ์ ์ถ๋ ฅํด๋ณด๋ ๋ฌธ์ 

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

- ์ค์ ํ์์ ์์๋๋ก ๋ธ๋์ ๊ฐ์ ์ ์ฅํด์ฃผ๋ฉด ๋๋ค
- ๋ฃจํธ๋ ๋ฌด์กฐ๊ฑด 1๋ฒ์ด๋ ๊ฐ์ ํ์ ๊ฐ์ฅ ์ผ์ชฝ ๋ฆฌํ๋ธ๋๋ถํฐ ์ซ์๋ฅผ ๋ฃ์ด์ฃผ๋ ์๊ณ ๋ฆฌ์ฆ



> ์์  ์ด์งํธ๋ฆฌ ํํ ์ค ๋ถ๋ชจ๋ธ๋๊ฐ ์์๋ธ๋๋ณด๋ค ํด๊ฒฝ์ฐ ๋ง์กฑํ ๋๊น์ง ๋ถ๋ชจ๋ธ๋์ ๊ฐ์ ๋ฐ๊พธ๋ ๋ฌธ์ 

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

- ๋งค ๋ธ๋์ ๊ทธ ๊ฐ์ ๋ฃ์ด์ฃผ๋ฉด์ definition์ ์ ์ฉ์์ผ์ค์ ๊ฐ๊ฐ์ ์กฐ์๋ธ๋์ ๋ค ์ ์ฉ์ ์์ผ์ค๋ค
- ์ดํ์ N๋ธ๋์ ์กฐ์๋ธ๋์ ๊ฐ๋ค์ ํฉ์ ๊ตฌํด์ฃผ๋ ๋ฌธ์ 
