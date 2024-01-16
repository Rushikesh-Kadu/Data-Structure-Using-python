class node:
    def __init__(self,data=None,next=None):
        self.item = data
        self.next = next

class SLL:
    def __init__(self):
        self.start = None

    def insertFirst(self,data):
        n = node(data,self.start)
        self.start = n

    def insertLast(self,data):
        n = node(data)
        if self.start == None:
            self.start = n
        else:
            temp = self.start
            while temp.next!=None:
                temp = temp.next
            temp.next = n
    
    def searchItem(self,data):
        if self.start!=None:
            temp = self.start
            while temp!=None:
                if temp.item==data:
                    return temp
                temp = temp.next
        return -1

    def insertAfter(self,after,data):
        if self.start!=None:
            t = self.searchItem(after)
            if t!=-1:
                n = node(data,t.next)
                t.next = n
    
    def removeFirst(self):
        if self.start!=None:
            self.start = self.start.next

    def removeLast(self):
        if self.start!=None:
            if self.start.next == None:
                self.start = None
            else:
                temp = self.start
                while temp.next.next!=None:
                    temp = temp.next
                temp.next = None
        
    def removeNode(self,data):
        if self.start !=None:
            t = self.searchItem(data)
            if t!=None:
                if t == self.start:
                    self.start = t.next
                else:
                    temp = self.start
                    while temp.next!=t:
                        temp = temp.next
                    temp.next = t.next
            
    def displayList(self):
        if self.start == None:
            print("Linked List is Empty")
        else:
            temp = self.start
            while temp!=None:
                print(temp.item,end=' ')
                temp = temp.next
            print()
            
    def __iter__(self):
        return SLLIterator(self.start)
    
class SLLIterator:
    def __init__(self,start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data

def menu():
    print("\n1.Insert First:")
    print("2.Insert Last:")
    print("3.Insert After:")
    print("4.Insert Delete First:")
    print("5.Insert Delete Last:")
    print("6.Insert Delete Item:")
    choice = int(input("Enter Your Choice:"))
    return choice



import os
# driver code
myList = SLL()
while True:
    os.system("cls")
    myList.displayList()
    match menu():
        case 1:
            data = eval(input("Enter Data:"))
            myList.insertFirst(data)
        case 2:
            data = eval(input("Enter Data:"))
            myList.insertLast(data)
        case 3:
            temp = eval(input("Enter data to insert After:"))
            data = eval(input("Enter Data:"))
            myList.insertAfter(temp,data)
        case 4:
            myList.removeFirst()
        case 5:
            myList.removeLast()
        case 6:
            data = eval(input("Enter Data:"))
            myList.removeNode(data)
        case _:
            print("Invalid Case")

    
    
