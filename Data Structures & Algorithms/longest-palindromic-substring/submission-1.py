class Solution:
    def longestPalindrome(self, s: str) -> str:
        # a substring sub of s is a palindrome if the string reads the same
        # forwards and backwards
        # that is, sub == sub[::-1]

        # for a string s, we can iterate through and look at each char ch
        # at ch, we can take the current char, and continue looking forward into the string
        # as we traverse through the string, we keep adding the forward char into the current char

        # say we have abcded
        # start at a -> add b -> add c -> add d -> add e add d no palindromes anywhere
        # then go to b, add c, add d, add e add d
        # then c, add d, add e add d
        # then d, add e, add d <- palindrome found, save maxcount = 3
        # then e, add d

        # this a brute force solution. we can find a more efficient solutions for sure

        # lets solve with 2d dp and solving this into smaller subcases
        # let dp[i][j] = true if the substring s=[i..j] is a palindrome
        # s[i..j] is a palindrome if s[i] == s[j], and s[i+1..j-1] is a palindrome
        # s[i+1..j-1] is a palindrome if s[i+2..j-2]
        # we need to build this bottom to top. we start at n-1..i
        # if length is 1, 2, or 3 (j - i <= 2) then matching ends is enough
        # we also keep track of the longest palindrome we have seen so far
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        resIdx = resLen = 0
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j] and (j-i <= 2 or dp[i+1][j-1] is True):
                    dp[i][j] = True
                    if (j - i + 1) > resLen:
                        resIdx = i
                        resLen = j - i + 1
        
        return s[resIdx:resIdx+resLen]