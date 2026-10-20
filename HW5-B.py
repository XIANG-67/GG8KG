a, b, k = map(int, input().split())

count = 0  # 紀錄倍數個數
total = 0  # 紀錄倍數總和

# 2. 使用 for 迴圈走訪閉區間 [a, b]
for i in range(a, b + 1):
    if i % k == 0:  # 整除判斷：餘數為 0 代表是 k 的倍數
        count += 1
        total += i

# 3. 印出個數與總和（中間自動以空白分隔）
print(count, total)