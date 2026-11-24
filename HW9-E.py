import math

# 判斷數字 num 是否為質數 (排除 < 2 的數，並檢查至 sqrt(num))
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True

# 讀取輸入兩個正整數 A 與 B
a, b = map(int, input().split())

# 自動調整搜尋區間的最小值與最大值
low, high = min(a, b), max(a, b)

# 搜尋區間內的所有質數
primes = [str(x) for x in range(low, high + 1) if is_prime(x)]

# 如果有質數則由小到大以空格隔開印出，否則印出空白行
if primes:
    print(" ".join(primes) + " ")
else:
    print()