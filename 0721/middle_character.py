# 문자열을 전달 받아 해당 문자열의 정중앙 문자를 반환하는 get_middle_char 함수를 작성하시오.
# 단, 문자열의 길이가 짝수일 경우에는 정중앙 문자 2개를 반환한다.

def get_middle_char(n):
    if len(n) == 0:
        return None
    if len(n) % 2 == 0:
        return n[int(len(n)//2)-1]+n[int(len(n)/2)]
    else:
        return n[int((len(n)-1)//2)]


print(get_middle_char('apple'))
print(get_middle_char('coding'))