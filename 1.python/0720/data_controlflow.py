# 1. 주어진 리스트의 요소는 학생 이름으로 구성되어 있다. 학생들의 수를 출력하시오.
students = ['김철수', '이영희', '박철']
print(len(students))


# 2. 이영희의 총 득표수를 출력하시오.
student = ['이영희', '김철수', '이영희', '박철', '김철수', '박철', '이영희', '이영희']
total=0
for i in student:
    if i == '이영희':
        total += 1
print(total)


# 3. 주어진 리스트의 요소 중에서 최댓값과 등장 횟수를 출력하시오.

numbers = [7, 10, 22, 7, 22, 22]
max=0
for i in numbers:
    if i >= max:
        max = i
count =0
for i in numbers:
    if i == max:
        count += 1

print(max,count)

# 4. apple에서 'a'를 모두 제거한 결과를 출력하시오.
word = 'apple'
for i in word:
    if i == 'a':
        continue
    print(i, end = '')

# 5. banana에서 해당 단어를 역순으로 뒤집은 결과를 출력하시오.
word_1 = 'banana'
print(word_1[::-1])

# 6. 입력으로 10이 주어진다. 정수 10의 약수를 오름차순으로 출력하는 프로그램 을 작성하시오.
N = 10
for divisor in range(1,N+1):
    if N % divisor == 0:
        print(divisor, end = ' ')

# 7. 높이가 4인 아래와 같은 내려가는 계단을 출력하시오.
# 1
# 1 2 
# 1 2 3 
# 1 2 3 4

numb = int(input())
for i in range(1,5):
    for j in range(1,i + 1):
        print(j, end = '')
    print()