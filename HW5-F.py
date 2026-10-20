n = int(input().strip())

# 2. 使用外層 for 迴圈控制列數 i（從 1 到 n）
for i in range(1, n + 1):
    row_str = ""
    # 3. 使用內層 for 迴圈控制欄數 j（從 1 到 n）
    for j in range(1, n + 1):
        # 計算 i * j，並使用 f-string 格式化為欄寬 4 靠右對齊
        row_str += f"{i * j:4d}"
    
    # 4. 印出該列的字串結果並自動換行
    print(row_str)
