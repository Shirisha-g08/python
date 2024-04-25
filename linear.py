'''pos=-1
def search(l,n):
    i=0
    while i<(len(l)):
        if l[i]==n:
           globals()['pos']=i
           return True
           i=i+1
           break
    else:
        return False
l=[1,5,7,3,8]
n=8
if search(l,n):
    print("Found",pos)
else:
    print("Not Found")'''

'''def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in i:
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
nums=[5,2,6,1,9,8]
sort(nums)
print(nums)'''


def fact(n):
    if n==0:
        return
    else:
        return n*fact(n-1)
print(fact(5))

