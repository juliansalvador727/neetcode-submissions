class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # order is our alphabet here
        # to check that each word is sorted lexicographically, we want it such that
        # a < b < c
        # lexicographically is such that
        # ord(a[i)) comes before ord(b[i]) etc...
        # and len(a) < len(b)
        
        order_index = {c: i for i,c in enumerate(order)}

        for i in range(len(words) -1):
            w1, w2 = words[i], words[i+1]
            for j in range(len(w1)):
                if j == len(w2):
                    return False
                
                if w1[j] != w2[j]:
                    if order_index[w1[j]] > order_index[w2[j]]:
                        return False
                    break
        return True

