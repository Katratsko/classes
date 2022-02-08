def countVowels(str):
    n = 0
    for i in str:
        if i in 'a, e, u, i, o':
            n+=1
    return n


a = countVowels('eifjgiohjrbgoa')
print(a)