N = int(input())

# 2. 讀取每位跑者的資料並儲存為 tuple (name, time, penalty) 放入 list 中 [1]
runners = []
for _ in range(N):
  # 使用解包直接拆解輸入字串，避免索引混淆
  name, time_str, penalty_str = input().split()
  time = int(time_str)
  penalty = int(penalty_str)

  # 嚴格符合限制：單筆紀錄必須儲存為不可變 tuple [1]
  runner_tuple = (name, time, penalty)
  runners.append(runner_tuple)


# 3. 定義多條件排序函式 [1]
# 傳回 (總秒數, 原始完賽秒數, 姓名字典序) 之比較 tuple
def get_sort_key(runner):
  runner_name, runner_time, runner_penalty = runner
  total_time = runner_time + runner_penalty
  return (total_time, runner_time, runner_name)


# 4. 執行多條件排序
sorted_runners = sorted(runners, key=get_sort_key)

# 5. 輸出排序結果（姓名與總秒數，以空白分隔） [1]
for runner in sorted_runners:
  runner_name, runner_time, runner_penalty = runner
  total_time = runner_time + runner_penalty
  print(f"{runner_name} {total_time}")