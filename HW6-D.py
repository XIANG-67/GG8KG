
N = int(input())

names = []
subtotals = []

for _ in range(N):
    line = input().split()
    name = line[0]
    price = int(line[1])
    quantity = int(line[2])
    
    pay_quantity = quantity - (quantity // 3)
    subtotal = price * pay_quantity
    
    names.append(name)
    subtotals.append(subtotal)

total = sum(subtotals)
if total >= 1000:
    total -= 100

top_index = 0
max_subtotal = subtotals[0]
for i in range(1, N):
    if subtotals[i] > max_subtotal:
        max_subtotal = subtotals[i]
        top_index = i

top_name = names[top_index]

for i in range(N):
    print(f"{names[i]} {subtotals[i]}")

print(f"TOTAL {total}")
print(f"TOP {top_name}")