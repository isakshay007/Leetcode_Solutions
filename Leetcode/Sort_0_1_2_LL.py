class ListNode:
    def __init__(self,data1=0,next1=None):
        self.data = data1
        self.next = next1

class Solution:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_Node = ListNode(data)
        if self.head is None:
            self.head = new_Node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_Node

    def sort_012(self):
        temp = self.head
        cnt_0=0
        cnt_1=0
        cnt_2=0
        while temp is not None:
            if temp.data == 0:
                cnt_0+=1
            elif temp.data ==1:
                cnt_1+=1
            elif temp.data ==2:
                cnt_2+=1
            temp = temp.next
        temp = self.head
        while temp is not None:
            if cnt_0:
                temp.data=0
                cnt_0-=1
            elif cnt_1:
                temp.data=1
                cnt_1-=1
            elif cnt_2:
                temp.data=2
                cnt_2-=1
            temp = temp.next


    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> " if temp.next else "")
            temp = temp.next
        print()

arr = [0,1,0,1,2,2,2,0,1]
ll=Solution()
for i in arr:
    ll.insert(i)
ll.display()
ll.sort_012()
ll.display()


