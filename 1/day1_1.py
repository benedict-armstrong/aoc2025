#!/usr/bin/env python3
from heapq import heapify, heappop

l1, l2 = [], []

with open("input.txt") as f:
    for line in f:
        i, j = map(int, line.split())
        l1.append(i)
        l2.append(j)

heapify(l1)
heapify(l2)

sum = 0

while l1:
    i = heappop(l1)
    j = heappop(l2)
    sum += abs(i - j)

print(sum)

# Complexity O(n *log(n))
