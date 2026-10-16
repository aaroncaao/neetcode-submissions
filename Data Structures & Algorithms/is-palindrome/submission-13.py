class Solution:
    def isPalindrome(self, s: str) -> bool:
        cl = "".join(c for c in s if c.isalnum()).lower()

        if cl == "":
            return True
        
        if cl[0] != cl[-1]:
            return False

        if len(cl) >= 1:
            for i in range(1, len(cl) // 2):
                if cl[i] != cl[-(i + 1)]:
                    return False
        return True