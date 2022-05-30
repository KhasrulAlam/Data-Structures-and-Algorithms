class Node:
    def __init__(self,data,next):
        self.data = data
        self.next= next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data, self.head)
        self.head= node

    def insert_at_ending(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next

        itr.next = Node(data,None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_ending(data)


    def print(self):
        if(self.head == None):
            print("Linked list is empty")
            return

        itr = self.head
        while itr:
            print(itr.data,'->',end='')
            itr = itr.next
        print('\n')

    def get_length(self):
        count =0;
        itr =self.head;
        while itr:
            itr=itr.next
            count+=1
        return count

    def remove_at(self,index):
        if(index<0 or index>=self.get_length()):
            raise Exception('This is not a valid index')
        itr = self.head
        if index==0:
            self.head=self.head.next
            return
        count=0
        while itr:
            if count+1 == index:
                break;
            count += 1
            itr = itr.next
        itr.next = itr.next.next

    def insert_at(self,data,index):
        if index<0 or index>self.get_length():
            raise Exception('Invalid index')

        if index==0:
            self.insert_at_begining(data)
            return
        count=0
        itr = self.head
        while itr:
            if count+1 == index:
                itr.next = Node(data, itr.next)
                break;
            itr =itr.next
            count+=1



ll = LinkedList()
ll.insert_values([10,20,30,40,50])
ll.print()
ll.insert_at_begining(15)
ll.print()
ll.insert_at_ending(35)
ll.print()
ll.remove_at(4)
ll.print()
ll.insert_at(52,3)
ll.print()
print("Length of this linked list:",ll.get_length())
