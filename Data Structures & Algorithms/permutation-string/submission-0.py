class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # maintain two frequency arrays
        # arr1 for s1
        # arr2 for a window in s2

        # if # the two arrays ever match, the window is a valid permutation
        # as we slide window forward, update counts by removing left character, and adding the new right character

        if len(s1) > len(s2):
            return False
        arr1, arr2 = [0] * 26, [0] * 26
        # build arr1 and arr2 up to len(s1) chars.
        for i in range(len(s1)):
            arr1[ord(s1[i]) - ord('a')] += 1
            arr2[ord(s2[i]) - ord('a')] += 1
        
        # count how many matches there are between arr1[i] and arr2[i]
        matches = 0
        for i in range(26):
            matches += (1 if arr1[i] == arr2[i] else 0)
        
        #slide a window from len(s1) in s1 up to len(s2) 
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            arr2[index] += 1
            if arr1[index] == arr2[index]:
                matches += 1
            elif arr1[index] + 1 == arr2[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord('a')
            arr2[index] -= 1
            if arr1[index] == arr2[index]:
                matches += 1
            elif arr1[index] - 1 == arr2[index]:
                matches -=1
            l += 1
        return matches == 26
        