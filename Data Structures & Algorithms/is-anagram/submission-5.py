class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if they have different lengths then they're not anagrams
        if len(s) != len(t):
            return False
        s_tracker = {}
        t_tracker = {}
        for i in range(len(s)):
            if s[i] not in s_tracker.keys():
                s_tracker[s[i]] = 0
        for i in range(len(t)):
            if t[i] not in t_tracker.keys():
                t_tracker[t[i]] = 0
        for i in range(len(s)):
            s_tracker[s[i]] += 1
        for i in range(len(t)):
            t_tracker[t[i]] += 1
        for key in s_tracker.keys():
            if key not in t_tracker.keys():
                return False
            if s_tracker[key] != t_tracker[key]:
                return False 
        return True