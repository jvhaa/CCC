# Canadian Computing Competition: 2014 Stage 1, Junior #1
# https://dmoj.ca/problem/ccc14j1

q= int(input())
s= int(input())
d= int(input())

if q== 60 and s== 60 and d== 60:
  print("Equilateral")
elif q+s+d==180 and q==s and q!=d:
  print("Isosceles")
elif q+s+d==180 and q==d and q!=s:
  print('Isosceles')
elif q+s+d==180 and s==d and s!=q:
  print('Isosceles')
elif q+s+d==180 and q!=s and q!=d and s!=d:
  print('Scalene')
elif q+s+d!=180:
  print('Error')
