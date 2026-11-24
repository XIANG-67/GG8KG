usage = int(input())

# 分段判斷電費計算
if usage <= 120:
    cost = usage * 2.10
elif usage <= 500:
    cost = 120 * 2.10 + (usage - 120) * 3.02
else:
    cost = 120 * 2.10 + (500 - 120) * 3.02 + (usage - 500) * 4.39

# 格式化輸出前綴與保留小數點第一位
print(f"NT${cost:.1f}")
