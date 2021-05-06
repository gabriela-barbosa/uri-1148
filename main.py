n, e = map(int, input().split())
route = []
v = n + 1
a = e

NUM_MAX = 9999

def dijkstra (origin, destiny):


while n != 0 and e != 0:
    items = []
    consult = []

    if not (1 <= n <= 500 and 0 <= e <= n * n):
        exit()

    for i in range(n):
        line = []
        for j in range(n):
            line.append(NUM_MAX)
        route.append(line)
    for i in range(e):
        x, y, h = map(int, input().split())
        # items.append((x, y, h))

        if not (1 <= x and y <= n and 1 <= h <= 1000):
            exit()

        if route[x][y] == NUM_MAX:
            route[x][y] = h
        else:
            route[x][y] = 0
            route[y][x] = 0

    k = int(input())

    if not (0 <= k <= 100):
        exit()
    for x in range(k):
        o, d = map(int, input().split())
        consult.append((o, d))
    n, e = map(int, input().split())
    v = n + 1
    a = e
