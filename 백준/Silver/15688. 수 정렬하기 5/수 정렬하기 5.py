import sys

num = int(sys.stdin.readline())
case = []
for _ in range(num):
  case.append(int(sys.stdin.readline()))

case.sort()
for i in case:
  print(i)