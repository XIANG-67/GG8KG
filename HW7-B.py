def is_prime(n):
    """使用試除法判定 n 是否為質數

    - 小於或等於 1 的整數不是質數
    - 檢查除數 d 從 2 開始，直到 d * d > n
    """
    if n <= 1:
        return False

    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1

    return True


def main():
    # 讀取區間 L 與 R
    L, R = map(int, input().split())

    # 依序對區間內的每一個數字呼叫 is_prime 函數進行篩選
    primes = [x for x in range(L, R + 1) if is_prime(x)]

    if primes:
        # 輸出所有質數（以空白分隔）
        print(" ".join(map(str, primes)))
        # 輸出個數與總和
        print(f"{len(primes)} {sum(primes)}")
    else:
        # 若區間內沒有質數
        print("NONE")
        print("0 0")


if __name__ == "__main__":
    main()