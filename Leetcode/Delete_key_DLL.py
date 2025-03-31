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

    def delete_key(self,key):
        temp = self.head
        while temp:
            if temp.data == key:

                if temp == self.head:
                    self.head = temp.next
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None

                elif temp == self.tail:
                    self.tail = temp.prev
                    if self.tail:
                        self.tail.next= None
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
               
                temp = temp.next
            else:
                temp = temp.next


    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end="<->" if temp.next else "")
            temp = temp.next
        print()



arr = [5,10, 20, 30, 10 , 20]
key = 10
ll = Double_LL()
for i in arr:
    ll.insert(i)
ll.display()
ll.delete_key(10)
ll.display()