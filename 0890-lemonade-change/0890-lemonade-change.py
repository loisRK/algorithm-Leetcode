class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = 0
        ten = 0
        cnt = 0

        if bills[0] > 5:
            return False

        for i in range(len(bills)):
            if bills[i] == 5:
                five += 1
            elif bills[i] == 10:
                if five > 0:
                    ten += 1
                    five -= 1
                else:
                    return False
            elif bills[i] == 20:
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                elif five >= 3 and ten == 0:
                    five -= 3
                else:
                    return False

            cnt += 1
        
        if cnt == len(bills):
            return True