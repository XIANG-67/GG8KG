n = int(input().strip())

# 2. 初始化反轉累積結果變數為 0
rev = 0

# 3. 使用 while 迴圈進行數字反轉（利用取餘數與整數除法）
# 當 n = 0 時迴圈不執行，rev 保持為 0
while n > 0:
    digit = n % 10         # 取得目前最右側的個位數
    rev = rev * 10 + digit # 將舊數值放大 10 倍並加上新個位數
    n = n // 10            # 去掉個位數

# 4. 輸出反轉後的整數
print(rev)

