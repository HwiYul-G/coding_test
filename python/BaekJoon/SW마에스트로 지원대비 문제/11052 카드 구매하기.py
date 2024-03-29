n = int(input())
p = [0] + list(map(int, input().split()))
dp = [0] * (n+1)
dp[1] = p[1]
for i in range(2, n+1):
    dp[i] = max(p[i], p[1]*i)
    for j in range(1, i//2+1):
        dp[i] = max(dp[i], dp[j] + dp[i-j])
print(dp[n])