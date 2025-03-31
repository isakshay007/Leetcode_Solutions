class ListNode:
    def __init__(self, data1=0, next1=None):
        self.data = data1
        self.next = next1

class Solution:
    def __init__(self):
        self.head = None
    
    def insert(self,data):
        new_Node = ListNode(data)
        if self.head is None:
            self.head = new_Node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_Node
    
    def reverse(self):
       
        temp = self.head
        prev = None
        
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        
        self.head = prev
        return self.head
   
    def add(self):
        
        self.reverse()
        temp = self.head
        carry=1

        while temp:
            temp.data += carry
            if temp.data<10:
                carry = 0
                break
            else:
                
                temp.data=0
                carry=1

            if carry == 1 and temp.next is None:
                temp.next=ListNode(1)
                carry=0
            temp = temp.next
        
        self.reverse()


    def display(self):
        
        temp = self.head
        
        while temp:
            print(temp.data,end = "->" if temp.next else "")
            temp = temp.next
        print()
    
arr = [0,9]
ll=Solution()
for i in arr:
    ll.insert(i)
ll.display()
ll.add()
ll.display()