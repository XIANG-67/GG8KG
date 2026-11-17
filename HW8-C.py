import sys
def solve():
     line1 = sys.stdin.readline()
    if not line1 or not line1.strip():
        return
    parts1 = line1.strip().split()
    N = int(parts1[0])  
    M = int(parts1[1])  
    line2 = sys.stdin.readline()
    raw_A = line2.strip().split() if line2 else []
    line3 = sys.stdin.readline()
    raw_B = line3.strip().split() if line3 else []
    set_A = set(raw_A)
    set_B = set(raw_B)
    inter = set_A & set_B
    union = set_A | set_B
    diff_A_B = set_A - set_B
    diff_B_A = set_B - set_A
     for res in [inter, union, diff_A_B, diff_B_A]:
        print(" ".join(sorted(res)) if res else "NONE")


if __name__ == "__main__":
    solve()