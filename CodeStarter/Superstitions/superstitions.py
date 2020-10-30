n, x = map(int, input().split())
a = [int(x) for x in input().split()]
count = 0
for i in range(n):
    for j in range(i + 1, n):
        if(a[i] + a[j] == x):
            count += 1
print(count)
