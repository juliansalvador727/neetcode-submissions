class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        for ch in s:
            if ch != "]":
                st.append(ch)
            else:
                substr = ""
                while st[-1] != "[":
                    substr = st.pop() + substr
                st.pop()

                k = ""
                while st and st[-1].isdigit():
                    temp = st.pop()
                    k = temp + k
                st.append(int(k) * substr)
        
        return "".join(st)
