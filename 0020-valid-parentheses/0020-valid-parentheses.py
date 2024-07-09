class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets={
            '[':']',
            '{':'}',
            '(':')'
        }
        stack=[]
        for b in s:
            if b in brackets.keys():
                stack.append(b)
            elif (not stack) or (brackets[stack.pop()] != b):
                return False

        if stack:
            return False
        else:
            return True
                    
