'''sentences=["alice and bob love leetcode","i think so too","this is great thanks very much"]
mcount=0
for sentence in sentences:
    words=sentence.split()
    count=len(words)
    mcount=max(mcount,count)
print(count)'''



'''operations=["--x","x++","x++"]
x=0
for i in range(len(operations)):
    if operations[i]=="x++" or operations[i]=="++x":
        x=x+1
    else:
        x=x-1 
print(x)      ''' 

'''hours = [0,1,2,3,4]
target = 2
count=0
for i in range(len(hours)):
    #count=0
    if hours[i]>=target:
        count+=1
print(count)'''


def revlist(self,head):
    prev_node=None
    current_node=head
    while current_node!=None:
        next_node=current_node.next
        current_node.next=prev_node
        prev_node=current_node
        current_node=next_node
l=[1,2,3,4]

