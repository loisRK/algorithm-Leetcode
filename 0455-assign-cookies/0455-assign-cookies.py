class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort(reverse=True)
        s.sort(reverse=True)
        cnt = 0
        chk = 0
        start = 0

        while chk!=len(g) and len(s)!=0:
            i=0
            for j in range(start, len(g)):
                if s[i] >= g[j]:
                    del g[j]
                    del s[i]
                    cnt += 1
                    i += 1
                    start = j
                    break
                chk += 1
        
        return cnt