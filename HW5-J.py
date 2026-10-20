s, d, t = map(int, input().split())

# 2. 初始化經過天數為 0
days = 0

# 3. 使用 while 迴圈每日更新存款與天數（禁止使用除法或數學公式）
# 若一開始 s >= t，則迴圈不執行，days 保持為 0
while s < t:
    s += d
    days += 1

# 4. 輸出最少天數
print(days)