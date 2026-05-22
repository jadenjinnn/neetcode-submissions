class Solution:
    def isPalindrome(self, s: str) -> bool:
        front, back = 0, len(s)-1

        while front<back:
            while not s[front].isalnum():
                front += 1
            
                if front == len(s):
                    return True

                
            while not s[back].isalnum():
                back -= 1

                if back == -1:
                    return True

            if not s[front].lower() == s[back].lower():
                return False
            else:
                front += 1
                back -= 1

        return True