class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp_arr = [[0] * (len(text2)+1) for i in range(len(text1)+1)]
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    dp_arr[i][j] = dp_arr[i+1][j+1] + 1
                else:
                    dp_arr[i][j] = max(dp_arr[i+1][j], dp_arr[i][j+1])
        return dp_arr[0][0]
        