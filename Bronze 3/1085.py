x, y, w, h = map(int, input().split())


def euclidean_distance(a, b, c, d):
    return ((a - c) ** 2 + (b - d) ** 2) ** (1/2)


h1 = h - y
h2 = y
h3 = x
h4 = w - x
h5 = euclidean_distance(0, h, x, y)
h6 = euclidean_distance(w, 0, x, y)
h7 = euclidean_distance(0, 0, x, y)
h8 = euclidean_distance(w, h, x, y)

print(min(h1, h2, h3, h4, h5, h6, h7, h8))

