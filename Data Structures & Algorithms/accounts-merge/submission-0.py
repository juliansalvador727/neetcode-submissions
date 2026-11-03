class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = list(range(len(accounts)))
        size = [1] * len(accounts)

        def find(name):
            while name != parent[name]:
                parent[name] = parent[parent[name]]
                name = parent[name]
            return name

        def union(a,b):
            u = find(a)
            v = find(b)

            if u == v:
                return False
            if size[u] <= size[v]:
                u, v = v, u
            parent[v] = u
            size[u] += size[v]

            return True
        account_owner = {}
        
        for idx, account in enumerate(accounts):
            for email in account[1:]:
                if email in account_owner:
                    union(idx, account_owner[email])
                else:
                    account_owner[email] = idx    
        
        groups = defaultdict()
        for email, owner in account_owner.items():
            root = find(owner)

            if root not in groups:
                groups[root] = []
            
            groups[root].append(email)
        
        result = []

        for root, emails in groups.items():
            name = accounts[root][0]
            result.append([name] + sorted(emails))
        return result



        

