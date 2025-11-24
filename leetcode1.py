class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def help_forward(s1, s2, start):
            ans = 0
            i = start
            for ch in s1:
                if i < len(s2) and ch == s2[i]:
                    ans += 1
                    i += 1
            return ans

        best1 = 0
        for i in range(len(text2)):
            best1 = max(best1, help_forward(text1, text2, i))

        def help_forward2(s1, s2, start):
            ans = 0
            i = start
            for ch in s2:
                if i < len(s1) and ch == s1[i]:
                    ans += 1
                    i += 1
            return ans

        best2 = 0
        for i in range(len(text1)):
            best2 = max(best2, help_forward2(text1, text2, i))

        return max(best1, best2)
