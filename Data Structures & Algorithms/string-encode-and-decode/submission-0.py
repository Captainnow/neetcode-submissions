class Solution:

    def encode(self, strs: List[str]) -> str:
        # Appends "length#string" for each word in a single linear pass
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            # 1. Find where the delimiter '#' ends to parse the length
            j = i
            while s[j] != '#':
                j += 1
                
            # 2. Extract the integer length of the upcoming string
            length = int(s[i:j])
            
            # 3. Read the actual string using string slicing
            start = j + 1
            end = start + length
            res.append(s[start:end])
            
            # 4. Move our pointer to the start of the next encoded block
            i = end
            
        return res
