n = int(input().strip())

# 2. 初始化前兩項 F(0) = 0, F(1) = 1
a, b = 0, 1

# 3. 使用 for 迴圈迭代 n 次更新數值（不使用遞迴）
# 當 n = 0 時迴圈不執行，印出 a (即 0)
# 當 n = 1 時迴圈執行 1 次，印出更新後的 a (即 1)
for _ in range(n):
    a, b = b, a + b

# 4. 輸出第 n 項結果
print(a)