"""import sys
n = int(input())
list = [list(map(int,sys.stdin.readline().split())) for _ in range (n)]

map = [[[0,[]] for i in range(n+1)] for j in range(n+1)]

for days in range (n):
    map[days][0] = [list[days][1],[days]]
    next_work_day = days+list[days][0]
    for j in range(n):
        if map[days][j][0]:
            work_pay = map[days][j][0]
            work_list = map[days][j][1]
            if days + 1 < n:
                pre_work_not_done = map[days+1][j]
                if work_pay > pre_work_not_done[0]:
                    map[days+1][j] = [work_pay,work_list]
            if next_work_day <= n:
                pre_work_done = map[next_work_day][next_work_day]
                if j == 0 and work_pay > pre_work_done[0]:
                    map[next_work_day][next_work_day] = [work_pay, work_list]
                    continue
                if j != 0 and work_pay + map[days][0][0] > pre_work_done[0]:
                    map[next_work_day][next_work_day] = [work_pay + map[days][0][0], work_list + [days]]
max_pay = 0
for i in range(n+1):
    for j in range(n):
        max_pay = max(max_pay, map[i][j+1][0])
print (max_pay)
"""

##===================================================================

import sys
N = int(input())
schedule = [list(map(int, sys.stdin.readline().split())) for _ in range (N)]

dp = [0 for i in range (N+1)]

for i in range(N):
    for j in range(i+schedule[i][0],N+1):
        if dp[j] < dp[i] + schedule[i][1]:
            dp[j] = dp[i] + schedule[i][1]
    print (dp)
print(dp[-1])