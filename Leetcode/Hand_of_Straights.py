from collections import Counter
class Solution:
    def isNStraightHand(self, hand, groupsize):
        
        if len(hand)%groupsize != 0:
            return False
        
        card_count = Counter(hand)

        sorted_cards = sorted(card_count.keys())

        for i in sorted_cards:
            while card_count[i]>0:
                for j in range(groupsize):
                    if card_count[i+j]==0:
                        return False
                    card_count[i+j]-=1

        return True
hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3
sol = Solution()
print(sol.isNStraightHand(hand,groupSize))
        