import sys


def solve():
    # 1. 讀取初始商品種類數 N
    first_line = sys.stdin.readline()
    if not first_line or not first_line.strip():
        return
    N = int(first_line.strip())

    # 符合限制：使用 dict 儲存「商品名稱 -> 庫存數量」
    inventory = {}

    # 2. 讀取 N 筆初始庫存
    for _ in range(N):
        line = sys.stdin.readline().strip()
        if not line:
            continue
        parts = line.split()
        item = parts[0]  # 正確加上 [0] 取出商品名稱
        stock = int(parts[1])  # 正確加上 [1] 取出庫存數量
        inventory[item] = stock

    # 3. 讀取指令數量 Q
    q_line = sys.stdin.readline()
    if not q_line or not q_line.strip():
        return
    Q = int(q_line.strip())

    successful_sales_qty = 0  # 成功售出總件數
    rejected_buy_count = 0  # 被拒絕的購買筆數

    # 4. 依序處理 Q 筆指令
    for _ in range(Q):
        line = sys.stdin.readline().strip()
        if not line:
            continue
        parts = line.split()
        op = parts[0]  # [0]: 指令 (ADD 或 BUY)
        item = parts[1]  # [1]: 商品名稱
        qty = int(parts[2])  # [2]: 數量

        if op == "ADD":
            # 增加庫存，若不存在則利用 get(item, 0) 初始化
            inventory[item] = inventory.get(item, 0) + qty

        elif op == "BUY":
            # 先用 in 檢查商品是否存在，且庫存充足 (>= qty)
            if item in inventory and inventory[item] >= qty:
                inventory[item] -= qty  # 扣除庫存 (降為 0 仍保留)
                successful_sales_qty += qty
            else:
                rejected_buy_count += 1  # 拒絕筆數 +1

    # 5. 輸出結果
    print(f"{successful_sales_qty} {rejected_buy_count}")

    # 依商品名稱字典序 (sorted) 輸出
    for item in sorted(inventory.keys()):
        print(f"{item} {inventory[item]}")


if __name__ == "__main__":
    solve()

