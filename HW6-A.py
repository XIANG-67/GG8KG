
B, N, R, C = map(int, input().split())
service_fee = (B * R) // 100
T = B + service_fee - C
if T < 0:
    T = 0
q = T // N   
r = T % N   
a = N - r    
b = r        
print(T)
print(f"{q} {a}")
print(f"{q + 1} {b}")
