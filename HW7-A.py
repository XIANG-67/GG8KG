def parking_fee(minutes):
    """根據停車分鐘數計算單次費用

    - 0 分鐘免費
    - 每開始 30 分鐘收 30 元（不足 30 分鐘以 30 分鐘計）
    - 單次費用上限為 200 元
    """
    if minutes == 0:
        return 0

    # 使用整數除法計算區間數（(minutes + 29) // 30 可自動將不足 30 分鐘的部分無條件進位）
    blocks = (minutes + 29) // 30
    fee = blocks * 30

    # 套用單次最高 200 元上限
    return min(fee, 200)


def main():
    # 讀取車輛數 N
    n = int(input().strip())

    # 讀取 N 個停車分鐘數
    minutes_list = list(map(int, input().split()))

    # 對每筆紀錄呼叫 parking_fee 函數
    fees = [parking_fee(m) for m in minutes_list]

    # 第一行輸出每輛車的費用（以空白分隔）
    print(" ".join(map(str, fees)))

    # 第二行輸出總費用
    print(sum(fees))


if __name__ == "__main__":
    main()