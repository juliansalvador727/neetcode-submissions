class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
                return (t := [i for i in range(n) if i not in {v for _, v in edges}], t[0] if len(t) == 1 else -1)[1]
