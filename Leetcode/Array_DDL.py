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
        new_node = Node(data)
        if self.tail is None:
            self.tail = self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_before_head(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_before_tail(self,data):
        new_node = Node(data)
        if self.head is None or self.head.next is None:
            self.insert_before_head(data)
            return
        
        tail = self.head
        
        while tail.next.next is not None:
            tail = tail.next

        new_node.next = tail.next
        new_node.prev = tail
        tail.next.prev = new_node
        tail.next = new_node
        
    def insert_before_kth(self,data,k):
        new_node = Node(data)
        if self.head is None or k==1:
            self.insert_before_head(data)
            return

        temp = self.head
        cnt=1
        while temp is not None and cnt<k:
            cnt+=1
            temp=temp.next
        
        if temp is None:
            self.insert_before_tail(data)
            return
        
        new_node.next = temp
        new_node.prev = temp.prev
        temp.prev.next = new_node
        temp.prev = new_node

    def insert_before_value(self,data,value):
        new_node = Node(data)
        if self.head is None or self.head.data == value:
            self.insert_before_head(data)
            return

        temp = self.head
        while temp is not None and temp.data!= value:
            temp=temp.next
        
        if temp is None:
            self.insert_before_tail(data)
            return
        
        new_node.next = temp
        new_node.prev = temp.prev
        temp.prev.next = new_node
        temp.prev = new_node
        
        

    def delete_head(self):
        if self.head == None or self.head.next == None:
            self.head = self.tail = None
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        temp.next = None
    
    def delete_tail(self):
        if self.head == None or self.head.next==None:
            self.head=self.tail=None
        temp = self.head
        while temp.next.next is not None:
            temp=temp.next
        temp.next = None
        self.tail =temp

    def delete_kth(self,k):
        if self.head==None or k<=0:
            return 
        if k==1:
            self.delete_head()
            return
        temp = self.head
        cnt = 1
        while temp and cnt<k:
            temp = temp.next
            cnt+=1
        if temp == None:
            return
        
        if temp == self.tail:
            self.delete_tail()
            return
        
        
        temp.prev.next = temp.next
      
        temp.next.prev = temp.prev
        temp.next = temp.prev = None
    
    def delete_value(self,value):
        if self.head==None:
            return 
        
        temp = self.head
        if temp.data==value:
            self.delete_head()
            return
        
        while temp:
            if temp.data == value:
                break
            temp = temp.next
        if temp == None:
            return

        if temp == self.tail:
            self.delete_tail()
            return
        
        temp.prev.next = temp.next
      
        temp.next.prev = temp.prev
        temp.next = temp.prev = None

    
    def reverse_dll(self):
        last = None
        current = self.head
        if self.head is None or self.head.next is None:
            return self.head
        while current is not None:
            last = current.prev
            current.prev = current.next
            current.next = last
            current = current.prev
        
        self.head = last.prev

        return self.head
  


    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end= "<->" if temp.next else "")
            temp =temp.next
        print()


arr = [5, 10, 20, 30]
ll = Double_LL()
for i in arr:
    ll.insert(i)
ll.display()
value=30
data=50
ll.insert_before_value(data,value)
ll.display()
