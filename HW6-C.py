G = int(input())
steps = list(map(int, input().split()))

total_steps = sum(steps)

target_days = 0
is_target = []
for s in steps:
    if s >= G:
        target_days += 1
        is_target.append(True)
    else:
        is_target.append(False)

max_val = max(steps)
max_days = []
for i in range(len(steps)):
    if steps[i] == max_val:
        max_days.append(str(i + 1))
max_days_str = " ".join(max_days)

max_consecutive = 0
current_consecutive = 0
for reach in is_target:
    if reach:
        current_consecutive += 1
        if current_consecutive > max_consecutive:
            max_consecutive = current_consecutive
    else:
        current_consecutive = 0

print(total_steps)
print(target_days)
print(max_days_str)
print(max_consecutive)