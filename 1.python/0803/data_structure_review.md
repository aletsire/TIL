# review_data_structure

## 1. 짝수리스트(List Comprehension)

1~10까지의 숫자중 짝수만 담긴 리스트 `even_list`

```python
even_list=[]
for i in range(1,11):
    if i%2 == 0:
        even_list.append(i)

print(even_list)
```

```python
even_list_1 = [i for i in range(1,11) if i%2 == 0]
print(even_list_1)
```



## 2. 곱집합(List Comprehension)

두 list의 가능한 모든 조합을 담은 `pair` 리스트

```python
girls = ['julia', 'anne', 'mary']
boys = ['evan', 'mark', 'jack']
```

```python
pair = []
girls = ['julia', 'anne', 'mary']
boys = ['evan', 'mark', 'jack']
for girl in girls:
    for boy in boys:
        pair.append((girl,boy))
print(pair)
```

```python
girls = ['julia', 'anne', 'mary']
boys = ['evan', 'mark', 'jack']
pair = [(girl, boy) for girl in girls for boy in boys]
print(pair)
```



## 3. 피타고라스정리(List Comprehension)

x < y < z < 50 내에서 피타고라스 방정식의 해

```python
result = []
for x in range(1, 50):
    for y in range(x, 50):
        for z in range(y, 50):
            if z**2 == y**2 + x**2:
                result.append((x, y, z))

print(result)
```

```python
result = [(x, y, z) for x in range(1, 50) for y in range(x, 50) for z in range(y, 50) if z**2 == y**2 + x**2]
print(result)
```



## 4. 모음 제거(List Comprehension)

문장에서 모음(a, e, i, o, u)를 모두 제거

```python
vowels = 'aeiou'
words = 'Music is My Life'
```

```python
vowels = 'aeiou'
words = 'Life is too short, you need python!'
new_words = []
for word in words:
    if word not in vowels:
        new_words.append(word)
print(''.join(new_words))
```

```python
result = [word for word in words if word not in vowels]
print(''.join(result))
```

