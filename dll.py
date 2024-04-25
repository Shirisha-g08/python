class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    '''def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            new.next=self.head
            self.head.prev=new
            self.head=new'''
    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            self.tail.next=new
            new.prev=self.tail
    
    def printing(self):
        i=self.head
        while i:
            print(i.data)
            i=i.next
    '''def reverse(self):
        prev=None
        current=self.head
        while current:
            if current.next==None:
                self.head=current
            current.next,current.prev=current.prev,current.next
            current=current.prev'''
    '''def deleteatbeg(self):
        self.head=self.head.next
        self.head.prev=None'''
    def deleteatend(self):
        self.tail=self.tail.prev
        self.tail.next=None
o=dll()
for i in range(1,6):
    #o.insertatbeg(i)
    o.insertatend(i)
#o.deleteatbeg()
o.deleteatend()
o.printing()
#o.reverse()

