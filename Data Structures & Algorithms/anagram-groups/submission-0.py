class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for s in strs:
            # Sorting the string creates a unique, hashable key for all anagrams
            key = "".join(sorted(s))
            groups[key].append(s)
            
        return list(groups.values())
