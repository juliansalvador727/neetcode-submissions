class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        if "0000" in visited or target in visited:
            return -1
        
        visited.add("0000")
        q = deque([("0000", 0)])
        steps = 0

        while q:
            lock, steps = q.popleft()
            if (lock == target):
                return steps

            for i in range(4):
                for x in [1, -1]:
                    digit = (int(lock[i]) + x) % 10
                    neighbor = lock[:i] + str(digit) + lock[i+1:]

                    if neighbor not in visited:
                        q.append((neighbor, steps+1))
                        visited.add(neighbor)

        return -1

