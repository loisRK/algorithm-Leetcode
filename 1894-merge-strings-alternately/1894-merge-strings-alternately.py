class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        output_word = ""
        longer = word1 if len(word1) >= len(word2) else word2
        shorter_len = len(word1) if len(word1) <= len(word2) else len(word2)
        for i in range(shorter_len):
            output_word += word1[i] + word2[i]
        output_word += longer[shorter_len:]
        return output_word