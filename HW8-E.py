# 1. 讀取紀錄筆數 N
N = int(input())

# 2. 讀取 N 筆紀錄，並使用 tuple 與 set 進行重複紀錄去重
records_set = set()
for _ in range(N):
  student, booth = input().split()
  # 限制 1 & 2：將每筆紀錄存成 tuple (student, booth)，並存入 set 中去重
  record_tuple = (student, booth)
  records_set.add(record_tuple)

# 3. 使用 dict 統計每位學生的不同攤位集章總數
stamp_counts = {}
for student, booth in records_set:
  # 限制 3：以 dict 統計每人獲得的章數
  stamp_counts[student] = stamp_counts.get(student, 0) + 1

# 4. 將統計結果存入 list 並進行雙條件排序
# 限制 4：以 list 儲存排序後的排行榜
ranking_list = list(stamp_counts.items())

# 排序規則：章數多的在前 (-count)，章數相同時姓名字典序較小者在前 (student)
ranking_list.sort(key=lambda x: (-x[1], x))

# 5. 輸出處理
# 第一行：印出有效集章總數 (即去重後的總筆數)
print(len(records_set))

# 後續：印出「姓名 章數」
for student, count in ranking_list:
  print(f"{student} {count}")