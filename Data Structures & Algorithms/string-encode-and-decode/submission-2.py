from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        # Time: O(N) | Space: O(N) to build the output string
        # Using a list comprehension inside "".join() is the fastest way to build strings in Python
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        # Time: O(N) | Space: O(1) auxiliary space (excluding the return list)
        res = []
        i = 0
        n = len(s)
        
        while i < n:
            # Find the position of the delimiter '#'
            # s.find() runs natively in C, making it faster than a manual while loop
            j = s.find('#', i)
            
            # Extract the string length and jump past the delimiter
            length = int(s[i:j])
            start = j + 1
            end = start + length
            
            # Extract the original string using fast C-optimized slicing
            res.append(s[start:end])
            
            # Advance the pointer to the next block
            i = end
            
        return res
