import sys


def solve():
    # 1. 讀取紀錄總筆數 N
    first_line = sys.stdin.readline()
    if not first_line or not first_line.strip():
        return
    N = int(first_line.strip())

    # 限制 1：必須使用 list 保存輸入紀錄，每筆為 tuple (user, item)
    records = []
    for _ in range(N):
        line = sys.stdin.readline().strip()
        if not line:
            continue
        parts = line.split()
        user = parts[0]  # 務必加上 [0] 取出姓名 (字串)
        item = parts[1]  # 務必加上 [1] 取出商品 (字串)
        records.append((user, item))  # 存入 tuple

    # 2. 讀取最後一行的 target 與 K
    last_line = sys.stdin.readline().strip()
    if not last_line:
        return
    target_part = last_line.split()
    target = target_part[0]  # 目標使用者
    K = int(target_part[1])  # 推薦上限數量 K

    # 限制 2：以 dict 將使用者對應到商品 set
    user_items = {}
    for r in records:
        u = r[0]  # 取出 tuple 的 user
        it = r[1]  # 取出 tuple 的 item
        if u not in user_items:
            user_items[u] = set()
        user_items[u].add(it)

    target_set = user_items.get(target, set())

    # 限制 3 & 4：透過交集 (&) 與差集 (-) 判斷相似使用者與候選商品，以 dict 累計分數
    candidate_scores = {}
    for u, items_set in user_items.items():
        if u == target:
            continue
        # 判斷相似使用者：至少買過一件與目標相同的商品 (交集 &)
        if items_set & target_set:
            # 候選商品：相似使用者買過但目標未買過 (差集 -)
            candidates = items_set - target_set
            for item in candidates:
                candidate_scores[item] = candidate_scores.get(item, 0) + 1

    # 限制 5：以 list 排序結果 (分數高者在前: -x[1]，同分依字典序: x[0])
    score_list = [(item, score) for item, score in candidate_scores.items()]
    sorted_candidates = sorted(score_list, key=lambda x: (-x[1], x[0]))

    # 3. 輸出結果
    if not sorted_candidates:
        print(0)
    else:
        R = min(K, len(sorted_candidates))
        print(R)
        for i in range(R):
            print(f"{sorted_candidates[i][0]} {sorted_candidates[i][1]}")


if __name__ == "__main__":
    solve()
    