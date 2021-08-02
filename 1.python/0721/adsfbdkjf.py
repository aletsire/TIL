def get_secret_word(a, b):
    val1 = 0
    val2 = 0
    for i in a:
        val1 += ord(i)
    for j in b:
        val2 += ord(j)
    if val1 > val2:
        return f"'{a}'"
    else:
        return f"'{b}'"

print(get_secret_word('tom', 'john'))