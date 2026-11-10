def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# 2. 計算三數最簡比例
def simplify_recipe(tea, milk, syrup):
    g = gcd(gcd(tea, milk), syrup)  # 找出三數的最大公因數
    return tea // g, milk // g, syrup // g


# 3. 主程式：讀取資料並輸出結果
N = int(input())
for _ in range(N):
    tea, milk, syrup = map(int, input().split())
    ans_tea, ans_milk, ans_syrup = simplify_recipe(tea, milk, syrup)
    print(ans_tea, ans_milk, ans_syrup)  # print 預設即以空白分隔輸出