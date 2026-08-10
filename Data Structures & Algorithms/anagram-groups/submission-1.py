# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         outputList = []
#         dict_of_seen_ones = {}
#         for i in strs:
#             if sorted(i) not in dict_of_seen_ones:
#                 dict_of_seen_ones[sorted(i)].push(i)
#         for j in dict_of_seen_ones:
#             outputList.append(dict_of_seen_ones.get(j))
#         return outputList

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}
        
        for word in strs:
            # 1. Sort the word and join it to form a hashable string key
            # key = "".join(sorted(word))
            key = str(sorted(word))
            
            # 2. Safely initialize with [] if absent, then append the word
            groups.setdefault(key, []).append(word)
            
        # 3. Return a list of all grouped lists directly
        return list(groups.values())