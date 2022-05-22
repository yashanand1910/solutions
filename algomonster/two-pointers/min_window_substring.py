def get_minimum_window(original: str, check: str) -> str:
    if len(check) > len(original): return '';
    count = { letter: 0 for letter in list(check) }
    for letter in list(check): count[letter] += 1

    left = 0
    while original[left] not in count:
        left += 1
    right = left
    if original[right] in count: count[original[right]] -= 1

    shortest = ''
    while right < len(original) - 1:
        flag = True
        for letter, n in count.items():
            if n > 0:
                flag = False
                break
        if flag:
            if shortest == '' or (right - left + 1) <= len(shortest):
                if shortest and (right - left + 1) == len(shortest):
                    shortest = min(shortest, original[left : right + 1])
                else:
                    shortest = original[left : right + 1]
            if original[left] in count: count[original[left]] += 1
            left += 1
            while original[left] not in count:
                left += 1
        else:
            right += 1
            if original[right] in count: count[original[right]] -= 1
    flag = True
    for letter, n in count.items():
        if n > 0:
            flag = False
    if flag:
        if shortest == '' or (right - left + 1) <= len(shortest):
            if shortest and (right - left + 1) == len(shortest):
                shortest = min(shortest, original[left : right + 1])
            else:
                shortest = original[left : right + 1]
    return shortest

if __name__ == '__main__':
    original = input()
    check = input()
    res = get_minimum_window(original, check)
    print(res)

