K = int(input())
S = input()

result = []
for c in S:
    if 'A' <= c <= 'Z':
        new_char = chr((ord(c) - ord('A') + K) % 26 + ord('A'))
        result.append(new_char)
    elif 'a' <= c <= 'z':
        new_char = chr((ord(c) - ord('a') + K) % 26 + ord('a'))
        result.append(new_char)
    else:
        result.append(c)

print("".join(result))
