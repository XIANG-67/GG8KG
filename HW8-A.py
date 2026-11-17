import sys


def solve():
    # 讀取第一行：初始歌曲數量 N
    line = sys.stdin.readline()
    if not line or not line.strip():
        return
    N = int(line.strip())

    # 讀取第二行：初始歌曲清單 (若 N=0 則讀取空白行)
    if N > 0:
        playlist = sys.stdin.readline().strip().split()
    else:
        sys.stdin.readline()  # 讀掉 N=0 時的空白行
        playlist = []

    # 讀取第三行：指令數量 Q
    Q_line = sys.stdin.readline()
    if not Q_line or not Q_line.strip():
        return
    Q = int(Q_line.strip())

    # 依序讀取 Q 行指令
    for _ in range(Q):
        cmd_line = sys.stdin.readline().strip()
        if not cmd_line:
            continue

        parts = cmd_line.split()
        op = parts[0]

        if op == "ADD":
            playlist.append(parts[1])
        elif op == "REMOVE":
            target = parts[1]
            if target in playlist:
                playlist.remove(target)
        elif op == "REVERSE":
            playlist.reverse()

    # 輸出最終狀態
    print(len(playlist))
    if len(playlist) == 0:
        print("EMPTY")
    else:
        print(" ".join(playlist))


if __name__ == "__main__":
    solve()