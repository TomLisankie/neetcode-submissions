class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "" or len(s) == 1:
            return True
        # get rid of all non-alphanumeric characters
        cleaned = "".join(filter(str.isalnum, s)).lower()
        # two pointer approach
        front_index = 0
        back_index = len(cleaned) - 1
        while front_index != back_index and front_index < back_index:
            if cleaned[front_index] != cleaned[back_index]:
                return False
            front_index += 1
            back_index -= 1
        return True

