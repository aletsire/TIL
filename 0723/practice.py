#1 세로로 출력하기
# number = 10
# for i in range(1,number+1):
#     print(i)

#2
# number = 5
# for num in range(number,-1,-1):
#     print(num)

# 3
# number = 10
# total = 0
# for num in range(number+1):
#     total += num
# print(total)

#02
#1
# number = 10
# for num in range(1,number+1):
#     if number % num == 0:
#         print(num, end = ' ')

#2
# numbers = [
#     85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
#     51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
#     52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24
# ]
# numbers_sort = sorted(numbers)
# print(numbers_sort[int((len(numbers_sort)-1)/2)])

#3
number = 4
for i in range(1,number+1):
    for j in range(1, i+1):
        print(j, end =' ')
    print()


