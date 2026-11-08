class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)

        res = set()

        def generate_subsets(i, cur, total):
            if total == target:
                res.add(tuple(cur))
                return
            if total > target or i == len(candidates):
                return
            
            cur.append(candidates[i])
            generate_subsets(i+1,cur,total+candidates[i])
            cur.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            generate_subsets(i+1,cur,total)

        generate_subsets(0,[],0)

        return [list(combination) for combination in res]