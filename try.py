'''try:
    l=[1,2,3]
    print(l[0])
except:
    print("index out of range")
finally:
    print("final block")'''



'''try:
    l=[1,2,3,4]
    raise ValueError()
except ValueError:
    print("value error")
finally:
    print("finall block")'''


'''interview question (output for this question =end of the block,out of index,final block)'''
def fun(l,ind):
    try:
        a=l.copy()
        a[0]=l[0]/l[ind]
    except ValueError:
        print("value error")
    finally:
        print("end of the block")

l=[1,2,3,4]
try:
    fun(l,5)
except IndexError:
    print("out of index")
finally:
    print("final block")




