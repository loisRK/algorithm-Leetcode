class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = []
        ten = []
        twenty = []
        cnt = 0

        if bills[0] > 5:
            return False

        for i in range(len(bills)):
            if bills[i] == 5:
                five.append(bills[i])
            elif bills[i] == 10:
                if len(five) > 0:
                    ten.append(bills[i])
                    del five[0]
                else:
                    return False
            elif bills[i] == 20:
                if len(five) > 0 and len(ten) > 0:
                    del five[0]
                    del ten[0]
                elif len(five) >= 3 and len(ten) == 0:
                    five = five[3:]
                else:
                    return False

            cnt += 1
        
        if cnt == len(bills):
            return True