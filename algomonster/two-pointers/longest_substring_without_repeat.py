def longest_substring_without_repeating_characters(s: str) -> int:
    left, right = 0, 0
    buffer = {}
    buffer[s[left]] = left
    length = 1
    while right < (len(s) - 1):
        if s[right + 1] not in buffer:
            right += 1
            buffer[s[right]] = right
        else:
            jump_to = buffer[s[right + 1]] + 1
            while left < jump_to:
                buffer.pop(s[left])
                left += 1
            right += 1
            buffer[s[right]] = right
        length = max(length, right - left + 1)
    return length
        
if __name__ == '__main__':
    s = input()
    res = longest_substring_without_repeating_characters(s)
    print(res)

