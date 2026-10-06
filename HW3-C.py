x1, x2, x3 = map(float, input().split())
m = (x1 + x2 + x3) / 3.0
v = ((x1 - m) ** 2 + (x2 - m) ** 2 + (x3 - m) ** 2) / 3.0
print(f"{m:.2f} {v:.2f}")