# 1. 讀取單一行輸入的整數 n
n = int(input().strip())

# 2. 初始化累乘變數為 1（滿足 0! = 1 的定義）
total = 1

# 3. 使用 for 迴圈從 1 累乘到 n
# 當 n = 0 時，range(1, 1) 不會執行，total 保持為 1
for i in range(1, n + 1):
    total *= i

# 4. 輸出計算結果
print(total)