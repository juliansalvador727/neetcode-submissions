class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        weaker = set(v for u,v in edges)
        teams = [i for i in range(n) if i not in weaker]
        return teams[0] if len(teams) == 1 else -1