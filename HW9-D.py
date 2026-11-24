n = int(input())

# 外層迴圈控制層數 (1 到 N)
for i in range(1, n + 1):
    # 內層迴圈控制每層輸出的數字個數與空格
    for j in range(i):
        print(f"{i} ", end="")
    print()  # 每層印完後換行
    