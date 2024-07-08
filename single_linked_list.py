class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class single_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    '''
    Len(): is used to caluculate the length of the list it returns and integer value
    syntax: obj.Len()
    '''
    def Len(self)-> int:
        count = 0
        temp = self.head
        if self.head == None:
            return 0
        while temp!=None:
            temp = temp.next
            count+=1
        
        return count
    '''
    Display function is used to display the data which is stored in the list
    syntax: obj.display()
    '''
    def display(self):
        temp = self.head
        if self.head == None:
            print("Empty")
        while temp != None:
            print(temp.data,end=" ")
            temp = temp.next
        print()

    '''
    insert_at_begining():   is a insert function which is used to insert the data into list "i.e" is at the begining it takes
    data as an argument which can be any datatype
    '''
    def insert_at_begining(self,data):
        temp = Node(data)
        if(self.head  == None):
            self.head = temp
            self.tail = temp
        else:
            temp.next = self.head
            self.head = temp
    
    '''
    insert_at_index():   is a insert function which is used to insert the data into list at specified position
     NOTE: position starts from 1 
     it takes
     data and pos (which is index where you want to insert) as an argument which can be any datatype
    '''
    def insert_at_index(self,data,pos):
        temp = Node(data)
        if pos < 2:
            self.insert_at_begining(data)
        
        cur = self.head
        pos-=1
        while(cur!=None and pos > 1):
            cur = cur.next
            pos-=1
        if cur!=None:
            temp.next = cur.next
            cur.next = temp
        else:
            print("Invalid position")

    '''
    insert_at_end():   is a insert function which is used to insert the data into list "i.e" is at the end it takes
    data as an argument which can be any datatype
    '''
    def insert_at_end(self,data):
        new_node = Node(data)
        temp = self.head
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    '''
    delete_at_begining():   is a delete function which is used to delete the data from list "i.e" is at the begining.
    ''' 
    def delete_at_first(self):
        temp = self.head
        if self.head == None:
            print("Invalid or list is EMPTY")
        if temp.next is not None:
            temp = temp.next
            self.head = temp
        #self.head = None
        if(self.head!= None and self.head.next == None):
            self.head = None
    '''
    delete_at_end():   is a delete function which is used to delete the data from list "i.e" is at the end.
    ''' 
    def delete_at_end(self):
        if self.head == None:
            print("EMPTY")
        temp = self.head
        while(temp.next!=self.tail):
            temp = temp.next
        if temp is not None and temp.next is not None:
            self.tail = temp
            self.tail.next = None
    '''
    deleteIndex():   is a delete function which is used to delete the data from list "i.e" is at the given index.
    Note: deleteIndex takes index as an argument
    ''' 
    def deleteIndex(self,index):
        temp = self.head
        cur = self.head
        if index == 1:
            self.delete_at_first()
        if index == self.Len():
            self.delete_at_end()
        if self.head is None:
            print("EMPTY")
        while(cur!=None and index>1):
            temp = cur
            cur = cur.next
            index -= 1
        if temp is not None and cur is not None:
            temp.next = cur.next
    '''
    update(): takes two arguments index and data
    update used to update the values in the list.
    '''
    def update(self, index,data):
        if self.head is None:
            print("EMPTY")
        temp = self.head
        while(temp is not None and index>1):
            temp = temp.next
            index-=1
        if temp is not None :
            temp.data = data


lst = single_linked_list()
lst.insert_at_begining(12)
lst.insert_at_begining(13)
lst.insert_at_begining(14)
lst.insert_at_index(1,3)
lst.insert_at_end(100)
lst.insert_at_end(150)

lst.display()
print("Head: ",lst.head.data)
print("Tail: ", lst.tail.data)
print("Length: ", lst.Len())
print("=======AFTER CHANGE========")
lst.delete_at_first()
lst.delete_at_end()
lst.deleteIndex(3)
lst.update(3,10)
lst.update(5,15)
lst.display()
print("Head: ",lst.head.data)
print("Tail: ", lst.tail.data)
print("Length: ", lst.Len())



            


