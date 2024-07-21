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
        gs = 0
        ss = 0
    

        while gs <= len(g)-1 and ss <= len(s)-1:
            if s[ss] >= g[gs]:
                gs += 1
                ss += 1
                cnt += 1
            else:
                gs += 1

        # while chk!=len(g) and len(s)!=0:
        #     i=0
        #     for j in range(start, len(g)):
        #         if s[i] >= g[j]:
        #             del g[j]
        #             del s[i]
        #             cnt += 1
        #             i += 1
        #             start = j
        #             break
        #         chk += 1
        
        return cnt