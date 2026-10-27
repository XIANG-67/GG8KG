M = int(input())

drink_names = []
drink_prices = []
drink_counts = []

for _ in range(M):
    name, price = input().split()
    drink_names.append(name)
    drink_prices.append(int(price))
    drink_counts.append(0)

N = int(input())

student_names = []
orders = []

for _ in range(N):
    s_name, d_name, qty_str = input().split()
    qty = int(qty_str)
    
    d_idx = drink_names.index(d_name)
    drink_counts[d_idx] += qty
    
    if s_name not in student_names:
        student_names.append(s_name)
    s_idx = student_names.index(s_name)
    
    orders.append((s_idx, d_idx, qty))

final_prices = []
for i in range(M):
    if drink_counts[i] >= 10:
        final_prices.append(drink_prices[i] - 5)
    else:
        final_prices.append(drink_prices[i])

student_totals = [0 for _ in student_names]
for s_idx, d_idx, qty in orders:
    student_totals[s_idx] += final_prices[d_idx] * qty

for i in range(M):
    print(f"DRINK {drink_names[i]} {drink_counts[i]}")

for i in range(len(student_names)):
    print(f"STUDENT {student_names[i]} {student_totals[i]}")

total_all = sum(student_totals)
print(f"TOTAL {total_all}")
