# Canadian Computing Competition: 2000 Stage 1, Junior #3, Senior #1
# https://dmoj.ca/problem/ccc00s1

quarter = int(input())
machines = {30: [int(input()), 35],
            60: [int(input()), 100],
            9: [int(input()), 10]}

time = 0

while quarter > 0:
    for quarters, machine in machines.items():
        if quarter <= 0:
            break
        time += 1
        quarter -= 1
        machine[0] += 1
        if machine[0] % machine[1] == 0:
            quarter += quarters

print(f"Martha plays {time} times before going broke.")
