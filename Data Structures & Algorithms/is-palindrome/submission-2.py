import string

class Solution:
    def isPalindrome(self, s: str) -> bool:

        new = s.translate(str.maketrans('', '', string.punctuation))
        new = new.replace(" ", "")
        new = new.lower()

        l = 0
        r = len(new) -1

        while l < r:
            if new[l] == new[r]:
                l+=1
                r-=1
            else:
                return False
            
        return True
