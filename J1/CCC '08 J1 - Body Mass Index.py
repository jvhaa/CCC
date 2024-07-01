# Canadian Computing Competition: 2008 Stage 1, Junior #1
# https://dmoj.ca/problem/ccc08j1

weight = float(input())
height = float(input())

bmi = weight / (height*height)

if bmi > 25:
    print("Overweight")
elif bmi < 18.5:
    print("Underweight")
else:
    print("Normal weight")
