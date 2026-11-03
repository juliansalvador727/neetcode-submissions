from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @cache
        def dfs(i):
            if i == len(s):
                return True
            for word in wordDict:
                if ((i + len(word)) <= len(s) and (s[i : i + len(word)] == word) and dfs(i + len(word))):
                    return True
            return False


        return dfs(0)