def anagramma(str1, str2):
    str1_sorted = list(str1)
    str1_sorted.sort()
    str2_sorted = list(str2)
    str2_sorted.sort()
    return str1_sorted == str2_sorted

a = anagramma('finder', 'friend')
print(a)
