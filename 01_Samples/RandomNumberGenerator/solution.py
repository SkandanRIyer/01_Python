def Sol(a, d):
    if d == len(a): return max(a)
    maxqueue = [0]
    for k in range(1, d):
        while maxqueue and a[k] > a[maxqueue[-1]]:
            maxqueue.pop()
        maxqueue.append(k)
    res = a[maxqueue[0]]
    for k in range(d, len(a)):
        if k - maxqueue[0] >= d: maxqueue.pop(0)
        while maxqueue and a[k] > a[maxqueue[-1]]:
            maxqueue.pop()
        maxqueue.append(k)
        res = min(res, a[maxqueue[0]])
    return res


N, Q = map(int, input().split())
a = list(map(int, input().split()))
for _ in range(Q):
    d = int(input())
    print(Sol(a, d))