# 1. 讀取輸入的兩行資料
n = int(input().strip())
scores = list(map(int, input().split()))

total_score = 0
pass_count = 0

# 2. 使用 for 迴圈逐筆處理成績（不使用 sum()）
for score in scores:
    total_score += score
    if score >= 60:  # 滿 60 分即為及格
        pass_count += 1

# 3. 計算平均值並格式化輸出（小數點後 2 位）
average = total_score / n

print(f"{average:.2f}")
print(pass_count)