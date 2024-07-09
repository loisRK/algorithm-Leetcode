class Solution(object):
    def removeStars(self, str):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for s in str:
            if s != '*':
                stack.append(s)
            else:
                stack.pop()

        return ''.join(stack)
        