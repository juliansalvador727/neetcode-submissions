class Solution:
    def countSubstrings(self, s: str) -> int:
        # we follow our pre-existing defined recurrence structure for a palindrome
        # let n be the length of string s
        # let dp[i][j] = true if s[i:j] is a palindrome
        # s[i:j] is a palindrome if s[i] == s[j] and s[i+1:j-1] is a palindrome
        # if s[i] == s[j] and (j - i + 1 <= 2 or dp[i+1][j-1]) then dp[i][j] = true
        # for i=n-1..0 for j=i..n

        # everytime our if evaluates to true, add 1 to counter. return counter at the end
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        count = 0
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i] == s[j] and (j - i + 1 <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    count += 1
        
        return count
