class Solution:
    def numDecodings(self, s: str) -> int:
        # find the relationship/recurrence
        # first, i want to store all 26 mappings in a hashmap
        mp = {}
        for i in range(1,27):
            mp[str(i)] = chr(ord("A") + i - 1)

        # lets first examine numbers 1-9 only and add 0 as a special case later.
        # 1-9 we evaluate 2 base cases
        # length of s is 1 and length of s is 2
        # if length of s is 1 then there is only 1 decoding
        # if length of s is 2 then there are two decodings, one char or two chars.
        
        # lets look at a case when s is 3
        # at s is 3, we can consume one letter, resulting in a string of size 2 and we know a string of
        # length 2 has two decodings
        # we can also consume two letters, resulting in a string of size 1, and we know a string of length 1 has one decoding
        # e.g. s="123"
        # AB
        # AW
        # LC

        # now lets consider having 0
        # if we have a len(s) = 1 and s = "0" then we have no decodings, so return 0
        # if we have len(s) = 2 we have to look at some options
        # we have "0x" where x is nonzero. then we have no decodings possible because 01 cannot be mapped, and if we map 1 we have just 0.
        # we have "x0", then we can have either 0 or 1 decodings depending on x. we can map 10 or 20 but nothing else

        #let dp[i] = number of ways to decode s[i:]
        n = len(s)
        dp = {n : 1}
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == '0':
                return 0
            res = dfs(i + 1)
            if i+1 < n and (s[i]=="1" or s[i] =="2" and s[i+1] in "0123456"):
                res += dfs(i + 2)
            dp[i] = res
            return res
            
        return dfs(0)