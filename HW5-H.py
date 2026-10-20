n = int(input().strip())

# 2. 初始化總和變數為 0
total = 0

# 3. 使用 while 迴圈取出個位數並相加（不使用字串走訪或 sum()）
# 當 n = 0 時迴圈不執行，total 保持為 0
while n > 0:
    total += n % 10  # 取出目前個位數
    n = n // 10      # 去掉個位數

# 4. 輸出各位數總和
print(total)