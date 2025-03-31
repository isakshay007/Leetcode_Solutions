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
    
    def find_pair(self,sum):
        ds=[]
        temp1 = self.head
        while temp1 is not None:
            temp2 = temp1.next
            while temp2 is not None and (temp1.data + temp2.data <= sum):
                if temp1.data + temp2.data == sum:
                    ds.append({temp1.data,temp2.data})
                temp2 = temp2.next
            temp1 = temp1.next
        print(ds)

    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end="<->" if temp.next else "")
            temp = temp.next
        print()

arr = [5,10, 14, 1, 12 , 3]
sum = 15
ll = Double_LL()
for i in arr:
    ll.insert(i)
ll.display()
ll.find_pair(15)