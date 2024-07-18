class Node:
    def __init__(self,data):
        self.next = None
        self.data = data
class circularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def Len(self) -> int:
        count = 1
        if self.head is None:
            return 0
        if self.head is not None and self.head.next is None:
            return 1

        temp = self.head
        while(temp!=None and temp.next!=self.head):
            temp = temp.next
            count+=1
                
        return count
    
    def display(self):
        if self.head is None:
            print("EMPTY")
            return
        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print()   
    def insertinto(self,data,index):
        new_node = Node(data)
        temp = self.head
        #cur = self.head

        if index<2:
            self.insert_at_first(data)
            return

        if index == self.Len()+1:
            self.insert_at_end(data)
            return

        else:
            index -= 1
            while(temp is not None and index>1):
                #cur = temp
                temp = temp.next
                index-=1
            
            new_node.next = temp.next
            temp.next = new_node



    def insert_at_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
            

    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            print("EMPTY")
            return
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node

    def deleteAt(self, index):
        if self.head is None:
            print("INVALID")
            return
        if index < 2:
            self.delete_at_first()
            return
        if index == self.Len():
            self.delete_at_end()
            return
        temp = self.head
        cur = self.head
        while(temp.next is not self.head and index > 1):
            cur = temp
            temp = temp.next
            index-=1
        cur.next = temp.next
        del temp
        

    def delete_at_first(self):
        if self.head is None:
            print("INVALID")
            return
        
        if self.Len() == 1:
            del self.head
        else:
            temp = self.head.next
            del self.head
            self.head = temp
            self.tail.next = self.head
        
    
    def delete_at_end(self):
        if self.head is None:
            print("INVALID")
        else:
            temp = self.head
            while(temp.next is not self.tail):
                temp = temp.next
            del self.tail
            self.tail = temp
            temp.next = self.head

    def update(self, data, index):
        if self.head is None:
            print("INVALID")
            return
        if index < 1:
            self.head.data = data
            return
        if index == self.Len():
            self.tail.data = data
            return
        temp = self.head
        while(temp is not None and index > 1):
            temp = temp.next
        
        temp.data = data

if __name__ == "__main__":
    lst = circularLinkedList()
    lst.insert_at_first(30)
    lst.insert_at_first(20)
    lst.insert_at_first(10)

    lst.insert_at_end(50)
    #lst.delete_at_first()
    #lst.delete_at_end()
    lst.deleteAt(2)
    lst.deleteAt(2)
    lst.display()
    print("Head: " ,lst.head.data)
    print("Tail: ", lst.tail.data)
    print("Length: ", lst.Len())
    print("=====================")
    lst.update(300, 2)
    lst.update(100,1)

    lst.display()

    print("Head: " ,lst.head.data)
    print("Tail: ", lst.tail.data)
    print("Length: ", lst.Len())