x, y, w, h = map(int, input().split())


def euclidean_distance(a, b, c, d):
    return ((a - c) ** 2 + (b - d) ** 2) ** (1/2)


h1 = h - y
h2 = y
h3 = x
h4 = w - x

print(min(h1, h2, h3, h4))

