def normalize(text):
    """將字串進行標準化整理：

    1. 只保留英文字母與數字 (isalnum)
    2. 將英文字母轉為小寫
    """
    result = []
    for char in text:
        if char.isalnum():
            result.append(char.lower())
    return "".join(result)


def is_palindrome(text, left, right):
    """使用遞迴判斷字串在 [left, right] 索引範圍內是否為回文

    解題限制：必須直接呼叫自身，不得使用迴圈、推導式、切片或 reversed()
    """
    # 基礎條件：當範圍交叉或重疊時（空字串、單一字元，或對稱比對完成），傳回 True
    if left >= right:
        return True

    # 兩端字元不相同，代表非回文
    if text[left] != text[right]:
        return False

    # 兩端字元相同，縮小索引範圍繼續遞迴比對
    return is_palindrome(text, left + 1, right - 1)


def main():
    import sys

    # 讀取一整行原始密語（完整讀取包含空白與符號的整行文字）
    text = sys.stdin.readline().rstrip("\r\n")

    # 進行字串標準化整理
    cleaned_text = normalize(text)

    # 呼叫遞迴函數判斷是否為回文
    if is_palindrome(cleaned_text, 0, len(cleaned_text) - 1):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()