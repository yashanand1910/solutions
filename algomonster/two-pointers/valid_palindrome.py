def is_palindrome(s: str) -> bool:
    s = s.lower()
    left, right = 0, len(s) - 1
    while right >= left:
        if not s[left].isalnum():
            left += 1
        if not s[right].isalnum():
            right += -1
        if s[left] != s[right]:
            return False
        left += 1
        right += -1
    return True

if __name__ == '__main__':
    s = input()
    res = is_palindrome(s)
    print('true' if res else 'false')

