class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        clean_s = s.lower().replace(" ","")
        clean_t = t.lower().replace(" ","")
        return sorted(clean_s)==sorted(clean_t)

        