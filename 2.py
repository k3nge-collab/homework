c = [2, 5, 8, 11, 14, 18, 21, 25, 30]
d = 18 # искомое число
l = 0
r = len(c) - 1
index = -1
while l <= r:
    mid=(l + r) // 2
    if c[mid]==d:
        index=mid
        break
    elif c[mid] < d:
        l=mid+1
    else:
        r=mid-1
print(index)