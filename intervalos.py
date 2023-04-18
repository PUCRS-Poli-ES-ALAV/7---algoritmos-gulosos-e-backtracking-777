def calcula_escalonamento(s, f, n):
    X = []
    i = 1

    while i <= n:
        X.append(i)
        k = i + 1
        while k <= n and s[k] <= f[i]:
            k = k + 1

        i = k
    return X

s = [2, 4, 1, 6, 4, 6,  7,  9,  9,  3, 13]
f = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

X = calcula_escalonamento(s, f, len(s)-1)

print(s)
print(f)


#for i in range(0, len(s)):

