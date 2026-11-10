def best_total(prices, index, remaining):
    """使用遞迴計算從索引 index 開始，在剩餘預算 remaining 下能花費的最大金額

    - 限制：必須直接呼叫自身，禁止使用迴圈、推導式、位元遮罩或 DP
    """
    # 基底條件：所有商品已考量完畢，或剩餘預算為 0
    if index == len(prices) or remaining == 0:
        return 0

    # 分支 1：不選擇目前商品
    option1 = best_total(prices, index + 1, remaining)

    # 分支 2：若預算足夠，選擇購買目前商品
    option2 = 0
    if prices[index] <= remaining:
        option2 = prices[index] + best_total(
            prices, index + 1, remaining - prices[index]
        )

    # 回傳兩分支的最大值
    return max(option1, option2)


def main():
    # 讀取 N (商品數) 與 B (預算)
    n, b = map(int, input().split())

    # 讀取 N 個商品價格
    prices = list(map(int, input().split()))

    # 從索引 0 與預算 B 開始呼叫遞迴函數並輸出結果
    print(best_total(prices, 0, b))


if __name__ == "__main__":
    main()
