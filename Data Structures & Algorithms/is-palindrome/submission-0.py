class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        print(s)
        if s is None:
            return True
        n = len(s) - 1
        l = 0
        while(l<n):
            if (s[l]) != s[n]:
                return False
            l += 1
            n -= 1
        return True
            

        