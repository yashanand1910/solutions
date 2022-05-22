from typing import List

def find_all_anagrams(original: str, check: str) -> List[int]:
    n = len(check)
    if n > len(original): return []
    letters = { letter: 0 for letter in list(check) }
    for letter in list(check): letters[letter] += 1

    left, right = 0, 0
    for i in range(n):
        if original[i] in letters:
            letters[original[i]] -= 1
    right = n - 1

    res = []
    flag = False
    for letter, count in letters.items():
        if count:
            flag = True
            break
    if not flag: res.append(left)

    while right < len(original) - 1:
        right += 1
        if original[right] in letters: letters[original[right]] -= 1
        if original[left] in letters: letters[original[left]] += 1
        left += 1
        flag = False
        for letter, count in letters.items():
            if count:
                flag = True
                break
        if not flag: res.append(left)
    return res

if __name__ == '__main__':
    original = input()
    check = input()
    res = find_all_anagrams(original, check)
    print(' '.join(map(str, res)))

