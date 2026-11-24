n_str = input().strip()
original_n = n_str
current_str = n_str
pass_count = 1

while True:
    # 將字串中的每個字元轉為整數後相加
    digit_sum = sum(int(ch) for ch in current_str)
    print(f"Pass {pass_count} : {digit_sum}")
    
    # 若計算結果為個位數 (<= 9)，代表已找到 Digital Root
    if digit_sum <= 9:
        break
    
    # 更新目前字串與計數器，繼續下一輪計算
    current_str = str(digit_sum)
    pass_count += 1

print(f"Digital Root of {original_n} : {digit_sum}")