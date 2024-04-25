class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            new=node(data)
            new.next=self.head
            self.head=new
    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            new=node(data)
            i=self.head
            while i.next:
                #i.next!=None
                i=i.next
            i.next=new
    def printing(self):
        i=self.head
        while i:
            print(i.data)
            i=i.next
    def findlength(self):
        count=0
        i=self.head
        while i:
            count+=1
            i=i.next
        return count
    def reversing(slef):
        prev=None
        current=self.head
        next=self.head.next
        while current:
            current.next=prev
            prev=current
            current=next
            if next:
                next=next.next
    self.head=prev

l=[1,2,3,4,5]
o=sll()
for i in l:
    o.insertatbeg(i)
    o.insertatend(i)
o.printing()
print(o.findlength())
