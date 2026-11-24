import sys  # 補上這行

# 讀取兩行輸入：第一行為密鑰串列，第二行為密文
key_input = sys.stdin.readline().strip()
cipher_text = sys.stdin.readline().rstrip('\r\n')

if key_input and cipher_text:
    keys = list(map(int, key_input.split()))
    key_len = len(keys)
    letter_count = 0
    plain_chars = []

    for ch in cipher_text:
        if 'A' <= ch <= 'Z':
            shift = keys[letter_count % key_len]
            # 大寫字母循環解密 (反向位移)
            new_ch = chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
            plain_chars.append(new_ch)
            letter_count += 1
        elif 'a' <= ch <= 'z':
            shift = keys[letter_count % key_len]
            # 小寫字母循環解密 (反向位移)
            new_ch = chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
            plain_chars.append(new_ch)
            letter_count += 1
        else:
            # 非英文字母原樣保留，且不增加 letter_count
            plain_chars.append(ch)

    print("".join(plain_chars))
    