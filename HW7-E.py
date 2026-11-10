import sys


def count_ways(step, n, blocked, memo):
    """使用記憶化遞迴計算到達第 n 階的走法數"""
    # 邊界條件：超過 N 階或踏中損壞階梯，走法數為 0
    if step > n or blocked[step]:
        return 0

    # 成功到達第 N 階，找到 1 種可行走法
    if step == n:
        return 1

    # 記憶化檢查：若該階梯的走法數已計算過，直接回傳結果
    if memo[step] != -1:
        return memo[step]

    # 遞迴計算：分別嘗試走 1 階與走 2 階，並記錄結果至 memo
    memo[step] = count_ways(step + 1, n, blocked, memo) + count_ways(
        step + 2, n, blocked, memo
    )
    return memo[step]


def main():
    # 讀取第一行 N (總階數) 與 K (損壞階數)
    first_line = sys.stdin.readline().split()
    if not first_line:
        return

    # 正確取得索引 [0] 與 [1] 並轉為整數
    n, k = int(first_line[0]), int(first_line[1])

    # 初始化 blocked 布林串列與 memo 記憶串列
    blocked = [False] * (n + 1)
    memo = [-1] * (n + 1)

    # 若有損壞階梯 (K > 0)，讀取第二行並標記 blocked 對應位置為 True
    if k > 0:
        broken_steps = map(int, sys.stdin.readline().split())
        for b in broken_steps:
            blocked[b] = True

    # 由 0 階開始呼叫遞迴函數並輸出總走法數
    print(count_ways(0, n, blocked, memo))


if __name__ == "__main__":
    main()