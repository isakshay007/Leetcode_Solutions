from typing import List

class Meeting:
    def __init__(self,start,end,pos):
        self.start = start
        self.end= end
        self.pos = pos

class Solution:

    
    def maxMeetings(self, start: List[int], end: List[int], n: int):

        meetings=[]
        for i in range(n):
            m= Meeting(start[i],end[i],i+1)
            meetings.append(m)
        
        meetings.sort(key = lambda x: (x.end,x.pos))
        
        result=[]
        last_end = meetings[0].pos
        result.append(last_end)

        for i in range(1,n):
            if meetings[i].start > last_end:
                result.append(meetings[i].pos)
                last_end = meetings[i].end
        return result

obj = Solution()
n = 6
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 5, 7, 9, 9]
print(obj.maxMeetings(start, end, n))