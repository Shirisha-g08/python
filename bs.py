l=[2,4,6,8,10]
si=0
li=len(l)-2
se=9
while si<=li:
    mid=si+li//2
    if l[mid]==se:
        print("ele found")
        break
    elif se<l[mid]:
        li=l[mid]-1
    else:
       si=l[mid]+1
else:
    print("not present")