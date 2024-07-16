class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class double_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def Len(self):
        count = 1
        if self.head is None:
            return 0
        temp = self.head
        while temp!=None and temp.next!=None:
            temp = temp.next
            count+=1
        return count
    
    def display(self):
        temp = self.head
        if self.head is None:
            print("EMPTY")
        print("[", end=" ")
        while(temp!=None):
            print(temp.data,end=" ")
            temp = temp.next
        print("]")

    def reverse(self):
        if self.head is None:
            print("EMPTY")
        temp = self.tail
        print("[",end=" ")
        while temp!=None:
            print(temp.data, end=" ")
            temp = temp.prev
        print("]")

    def insert_at_begining(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.tail = self.head
            self.head = new_node

    def insert_at_end(self,data):
        new_node = Node(data)
        temp = self.head
        if self.head is None:
            print("EMPTY")
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
    def insertIndex(self,Index,data):
        new_node = Node(data)

        if self.head is None:
            print("EMPTY")

        if Index<2:
            self.insert_at_begining(data)

        if Index>self.Len():
            self.insert_at_end(data)

        temp = self.head
        cur = self.head

        while(temp!=None and Index>1):
            cur = temp
            temp = temp.next
            Index-=1

        cur.next = new_node
        new_node.prev = cur
        new_node.next = temp
        temp.prev = new_node


    def delete_at_begin(self):
        temp = self.head
        if self.head is None:
            print("ALREADY EMPTY")
        if self.head is not None and self.head.next is None:
            self.head = None
        else:
            temp = temp.next
            self.head = temp
            self.head.prev = None
            

    
    def delete_at_end(self):
        #temp = self.head
        if self.head is None:
            print("EMPTY")
        if self.head is not None and self.head.next is None:
            self.head = None
            self.tail = None
        
        self.tail = self.tail.prev
        self.tail.next = None


    def deleteIndex(self,Index):
        if self.head is None:
            print("INVALID INDEX")
        if Index < 2:
            self.delete_at_begin()
        if Index == self.Len():
            self.delete_at_end()
        if Index > self.Len():
            print("Invalid Index")
        else:
            temp = self.head
            cur = self.head
            #Index-=1
            while temp!=None and Index>1:
                cur = temp
                temp = temp.next
                Index-=1
        
            cur.next = temp.next
            temp.next.prev = cur
            del temp
        
        
        

    def update(self,index,data):
        if self.head is None:
            print("EMPTY")
        if index<2:
            self.head.data = data
        if index == self.Len():
            self.tail.data = data
        else:
            temp = self.head
            while(temp!=None and index>1):
                temp = temp.next
                index-=1
            temp.data = data
        
    

lst = double_linked_list()
lst.insert_at_begining(10)
lst.insert_at_begining(0)
lst.insert_at_end(50)
lst.insert_at_end(60)
lst.insertIndex(2,20)
lst.insertIndex(4,30)
lst.insertIndex(5,40)
lst.display()
print("Head: ",lst.head.data)
print("Tail: " ,lst.tail.data)
print("Length: ",lst.Len())
print("======AFTER CHANGE=======")
lst.delete_at_begin()
lst.delete_at_begin()
lst.delete_at_end()
lst.deleteIndex(5)
lst.update(3, 100)
lst.display()
print("Head: ",lst.head.data)
print("Tail: " ,lst.tail.data)
print("Length: ",lst.Len())
lst.reverse()