# Canadian Computing Competition: 2000 Stage 1, Junior #4, Senior #2
# https://dmoj.ca/problem/ccc00s2

rivers = []

for i in range(int(input())):
  rivers.append(int(input()))


while True:
  action = int(input())
  if action == 99:
    river = int(input()) - 1
    per = int(input())
    stream = rivers[river]
    stream1 = (stream*per)/100
    stream2 = (stream*(100-per))/100
    rivers.pop(river)	
    rivers.insert(river, stream2)
    rivers.insert(river, stream1)
  elif action == 88:
    stream = int(input())
    rivers[stream-1] += rivers.pop(stream)
  else:
    break
print(*rivers)
