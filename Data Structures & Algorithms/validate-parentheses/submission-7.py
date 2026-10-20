class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        closed = { ")" : "(", "]" : "[", "}" : "{"}

        for ch in s:
            if ch in closed:
                if st and st[-1] == closed[ch]:
                    st.pop()
                else:
                    return False
            else:
                st.append(ch)
        
        return True if not st else False