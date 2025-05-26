a = [[5, 3, 2], [8, 6, 3], [3, 5, 2], [3, 6], [3, 7, 4], [2, 9]]
K = 3

res = []
for i in a:
    if(a.index(i) % (K-1) == 0):
        i.reverse()
        res.append(i)
    else:
        res.append(i)

print("After reversing every Kth row: " + str(res))