n, e = map(int, input().split())
MAX = 99999


def init_array(array, size):
    for r in range(size):
        line = []
        for s in range(size):
            element = 0
            if r != s:
                element = MAX
            line.append(element)
        array.append(line)


def dijkstra(origin, destiny, vert, map):
    mark, cost = [], []
    for i in range(vert):
        cost.append(MAX)
        mark.append(0)
    cost[origin] = 0
    current = origin
    while current != destiny:
        min = MAX
        mark[current] = 1
        for j in range(vert):
            if cost[j] > cost[current] + map[current][j]:
                cost[j] = cost[current] + map[current][j]
            if cost[j] < min and not (mark[j]):
                min = cost[j]
                current = j
        if min == MAX:
            print("Nao e possivel entregar a carta")
            return
    print(cost[destiny])


while n != 0 and e != 0:
    route = []

    if not (1 <= n <= 500 and 0 <= e <= n * n):
        exit()

    init_array(route, n)
    for i in range(e):
        x, y, h = map(int, input().split())

        if not (1 <= x and y <= n and 1 <= h <= 1000):
            exit()

        if route[y - 1][x - 1] != MAX:
            route[x - 1][y - 1] = 0
            route[y - 1][x - 1] = 0
        else:
            route[x - 1][y - 1] = h

    k = int(input())

    if not (0 <= k <= 100):
        exit()
    for x in range(k):
        o, d = map(int, input().split())
        dijkstra(o - 1, d - 1, n, route)
    n, e = map(int, input().split())
