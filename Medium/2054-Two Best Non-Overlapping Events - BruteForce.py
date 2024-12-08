class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        summax = 0  
        for i in range(len(events)):
            for j in range(len(events)):
                if i == j:
                    continue 
                if events[i][1] < events[j][0]:  
                    summax = max(summax, events[i][2] + events[j][2])
                elif events[i][0] > events[j][1]:  
                    summax = max(summax, events[i][2] + events[j][2])

        for event in events:
            summax = max(summax, event[2])
        
        return summax