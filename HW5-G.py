total = 0

# 2. 讀取第一筆輸入
num = int(input().strip())

# 3. 使用 while 迴圈檢查哨兵值 0
# 當 num 不為 0 時進行累加並讀取下一筆；若 num 為 0 則不進入迴圈
while num != 0:
    total += num
    num = int(input().strip())

# 4. 輸出最終總和結果
print(total)