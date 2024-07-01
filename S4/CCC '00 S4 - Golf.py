# Canadian Computing Competition: 2000 Stage 1, Senior #4
# https://dmoj.ca/problem/ccc00s4

length = int(input())

clubs = [int(input()) for i in range(int(input()))]

def lis_edit():
  n = length
  dp = [float('inf')] * (n+1)
  dp[0] = 0
  for i in range(1,n+1):
    for club in clubs:
      if i >= club:
        dp[i] = min(dp[i], dp[i-club]+1)
  return dp[n]

used = lis_edit()

print(f"Roberta wins in {used} strokes." if used != float('inf') else "Roberta acknowledges defeat.")
