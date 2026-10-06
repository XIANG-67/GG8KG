N = int(input())
a = N // 100
b = (N // 10) % 10
c= N % 10
print(f"{a} {b} {c}")
print(a + b + c)
print(a * b * c)
reversed_N = c * 100 + b * 10 + a
print(reversed_N)