from typing import List

LETTERS = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

def letter_combinations_of_phone_number(digits: str) -> List[str]:
    list = []
    def dfs(path):
        if len(path) == len(digits):
            list.append(''.join(path))
            return
        for i in LETTERS[digits[len(path)]]:
            path.append(i)
            dfs(path)
            path.pop()
    dfs([])
    return list

if __name__ == '__main__':
    digits = input()
    res = letter_combinations_of_phone_number(digits)
    print(' '.join(res))
