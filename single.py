'''single inheritance
class a:
    def fun1(self):
        print("fun1")
    def fun2(self):
        print("fun2")         
class b(a):
    def fun3(self):
        print("fun3")
    def fun4(self):
        print("fun4")
o=a()
p=b()
p.fun1()'''


'''multiple inheritance
class a:
    branch="cse"
    def __init__(self,x):
        self.x=x

    def fun1(self):
        print("fun1")
        print(self.x)
        print(a.branch,o.x)
    def fun2(self):
        print("fun2")
class b:
    def __init__(self):
        print("1")
    def fun(self):
        print("fun3")
    def fun(self):
        print("fun4")
class c(a,b):
    def fun(self):
        print("fun")
o=a(5)
p=b()
q=c()
#q.fun2()
q.fun(10)
#p.fun()
o.fun1()'''

'''variables in inheritance
class a:
    branch='cse'
    def __init__(self,x):
        self.x=x
    def fun(self):
        print(o.x,a.branch)
        
o=a(5)
o.fun()'''



class a:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(self.a+self.b)
class b(a):
    def fun(self):
        pass
p=a(5,4)
p.add()
q=b(4,4)
q.add()


        