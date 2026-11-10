b = [29, 10, 14, 37, 13]
g = len(b)
for i in range(g - 1):
    m = i
    for f in range(i + 1, g):
        if b[f] < b[m]:
            m = f
    b[i], b[m] = b[m], b[i]# Меняем местами
    print(b)
