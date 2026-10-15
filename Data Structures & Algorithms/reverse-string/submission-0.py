class Solution:
    def reverseString(self, s: List[str]) -> None:
        temp = s[0]
        s[0] = s[-1]
        s[-1] = temp  
    
        for i in range(1, len(s) // 2):  
            temp = s[i]
            s[i] = s[-(i + 1)]
            s[-(i + 1)] = temp         
    