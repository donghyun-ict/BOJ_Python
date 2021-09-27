import sys
import heapq

input = sys.stdin.readline

N = int(input())

card = []
for i in range(N):
    heapq.heappush(card, int(input()))

ans = 0
for i in range(N-1):
    value = heapq.heappop(card) + heapq.heappop(card)
    ans += value
    heapq.heappush(card, value)

print(ans)