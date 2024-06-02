class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged_str = ""
        length = max(len(word1), len(word2))

        for n in range(length):
            if n < (min(len(word1), len(word2))):
                merged_str = merged_str + word1[n]
                merged_str = merged_str + word2[n]


        if length == len(word2):
            return merged_str + word2[len(word1):]
        else:
            return merged_str + word1[len(word2):]

        