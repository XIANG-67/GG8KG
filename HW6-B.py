raw_input = input()
cleaned = "_".join(raw_input.lower().split())
is_valid_len = 6 <= len(cleaned) <= 16
allowed_chars = "abcdefghijklmnopqrstuvwxyz0123456789_"
is_valid_char = all(c in allowed_chars for c in cleaned) if cleaned else False
print(cleaned)
if is_valid_len and is_valid_char:
    print("VALID")
else:
    print("INVALID")