class Solution:
    def differ_by_one(self, str1, str2):
        if len(str1) != len(str2):
            return False
        return sum(1 for c1, c2 in zip(str1, str2) if c1 != c2) == 1
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set()

        q = deque()

        q.append((beginWord,1))
        visited.add(beginWord)

        min_count = 1
        

        while q:
            word, min_count = q.popleft()
            if word == endWord:
                return min_count

            for w in wordList:
                if self.differ_by_one(w, word) and w not in visited:
                    q.append((w, min_count+1))
                    visited.add(w)
        return 0

