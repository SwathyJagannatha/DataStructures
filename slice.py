from itertools import islice

a = [[5, 3, 2], [8, 6, 3], [3, 5, 2], [3, 6], [3, 7, 4], [2, 9], [3, 5, 2], [3, 6], [3, 7, 4], [2, 9]]
K = 3

for i in range(K-1, len(a), K):
    a[i] = list(islice(reversed(a[i]), len(a[i])))

print("After reversing every Kth row: " + str(a))