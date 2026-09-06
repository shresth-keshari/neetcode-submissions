class Solution:

    def encode(self, strs: List[str]) -> str:
        chunks = []
        for s in strs:
            chunks.append(f"{len(s)}#{s}")
        return "".join(chunks)


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i< len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            i = j+1+length
            res.append(s[j+1 : i])
        return res