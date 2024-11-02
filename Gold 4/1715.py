from queue import PriorityQueue

N = int(input())
pq = PriorityQueue()

for i in range(N):
    pq.put(int(input()))

result = 0
while pq.qsize() > 1:
    card1 = pq.get()
    card2 = pq.get()
    temp = card1 + card2
    result += temp
    pq.put(temp)

print(result)
