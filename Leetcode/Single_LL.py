class Node:
    def __init__(self,data1,next1=None):
        self.data = data1
        self.next = next1

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def insert_head(self,data):
        new_Node = Node(data)
        new_Node.next = self.head
        self.head = new_Node 
    
    def insert_tail(self,data):
        if self.head is None:
            return None
        new_Node = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_Node
        new_Node.next = None
    
    def insert_kth(self,data,k):
        if self.head is None:
            if k == 1:
                new_Node = Node(data)
                self.head  = new_Node
            else:
                return None
        if k==1:
            new_Node = Node(data)
            new_Node.next = self.head
            self.head  = new_Node
        cnt = 1
        temp = self.head
        while temp is not None and cnt<k-1:
            temp = temp.next
            cnt+=1
        if temp is None:
            return None
        else:
            new_Node = Node(data)
            new_Node.next = temp.next
            temp.next = new_Node
    
    def insert_value(self,data,val):
        if self.head is None:
            return None
        if self.head.data == val:
            new_Node = Node(data)
            new_Node.next = self.head
            self.head  = new_Node
            return self.head
        
        temp = self.head
        while temp.next is not None:
            if temp.next.data == val:
                new_Node = Node(data)
                new_Node.next = temp.next
                temp.next = new_Node
                return self.head
            temp = temp.next

    
    def length(self):
        temp = self.head
        cnt=0
        while temp:
            cnt+=1
            temp = temp.next
        return cnt
    
    def search(self,val):
        temp = self.head
        while temp is not None:
            if temp.data == val:
                return True
            temp = temp.next
        return False

    def delete_first(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        return self.head
    
    def delete_tail(self):
        if self.head is None or self.head.next is None:
            return None
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None
        return self.head


    def delete_kth(self,k):
        if self.head is None:
            return None
        temp = self.head
        if k==1:
            self.head = self.head.next
            return self.head
        if k > self.length():
            return None
        cnt = 1
        prev = None
        while temp is not None:
            if cnt == k:
                prev.next = prev.next.next
                return self.head
            prev = temp
            temp = temp.next
            cnt+=1

    def delete_value(self,value):
        if self.head is None:
            return None
        temp = self.head
        if temp.data == value:
            self.head = self.head.next
            return self.head
        if value > self.length():
            return None
        prev = None
        while temp is not None:
            if temp.data == value :
                prev.next = prev.next.next
                return self.head
            prev = temp
            temp = temp.next
        return None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end="->" if temp.next else "")
            temp = temp.next
        print()
arr = [2,4,6,7,5,1,0]
ll = LinkedList()
for i in arr:
    ll.insert(i)
data = 100
ll.display()
ll.insert_value(100,1)
ll.display()