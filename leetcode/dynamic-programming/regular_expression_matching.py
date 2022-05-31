from functools import lru_cache

class Solution:
    @lru_cache(None)
    def isMatch(self, s: str, p: str) -> bool:
        if not s:
            if not p: return True
            if len(p) > 1 and p[1] == '*': return self.isMatch(s, p[2:])
            return False

        if not p:
            return False

        if s[0] == p[0] or p[0] == '.':
            if len(p) > 1:
                if p[1] == '*':
                    return self.isMatch(s[1:], p) or self.isMatch(s[1:], p[2:]) or self.isMatch(s, p[2:])
            return self.isMatch(s[1:], p[1:])

        if len(p) > 1:
            if p[1] == '*':
                return self.isMatch(s, p[2:])

        return False


