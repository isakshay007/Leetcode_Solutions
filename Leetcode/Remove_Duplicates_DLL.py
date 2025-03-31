class Node:
    def __init__(self,data1,next1=None,prev1=None):
        self.data = data1
        self.next = next1
        self.prev = prev1

class Double_LL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self,data):
        new_Node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_Node
        else:
            self.tail.next = new_Node
            new_Node.prev = self.tail
            self.tail = new_Node
    
    def remove_duplicates(self):
        temp = self.head
        while temp and temp.next:
            next_Node = temp.next
            while next_Node is not None and next_Node.data == temp.data:
                next_Node = next_Node.next
            temp.next = next_Node
            if next_Node:
                next_Node.prev = temp
                temp = temp.next
        return self.head
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end="<->" if temp.next else "")
            temp = temp.next
        print()

arr = [1,1,2,2,2,3,4,4,4]
ll = Double_LL()
for i in arr:
    ll.insert(i)
ll.display()
ll.remove_duplicates()
ll.display()
