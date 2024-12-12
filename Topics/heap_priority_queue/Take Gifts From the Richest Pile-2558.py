class Solution(object):
    def pickGifts(self, gifts, k):
        for i in range(k):
            a = gifts.index(max(gifts))
            b = math.sqrt(gifts[a])
            gifts[a] = int(b)

        return sum(gifts)