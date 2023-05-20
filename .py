import sys
from math import*
input = sys.stdin.readline
n, k = map(int, input().split())
arr = [ x for x in range(1, n+1) ]

tmp = k-1; result = []

for i in range(n):
  if tmp >= len(arr): # k번째 왔을 때
    tmp %= len(arr)
    result.append(gcd(tmp, arr[tmp]))
  else:     
    tmp += 1

print(result)  