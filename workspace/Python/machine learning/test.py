import numpy as np
import random

'''a=np.empty((3,3),dtype=np.int64)
for i in a:
    for j in i:
        print(j)


k=np.empty((3,1),dtype=np.int64)
for i in range(0,2):
    for j in range(0,1):
        print(j)
    print('\n')
print(np.dot(obh.input_layer_weight,k))
a=[]
for i in range(0,3):
    a.append([random.randint(0,5)])
a = np.array(a)
print(a)
a=a.transpose()
print(a)'''
#print(np.multiply(obh.input_layer_weight,obh.hidden_layer_weight))

'''a=np.array([[1,2],[3,4]])
b=np.array([[2,3],[1,3]])
print(a,b)
print(np.subtract(a,b))'''
''' print('e=',error)
    print('t',target)
    print('g',Guess)
'''
for i in range(0,3):
    a.append([random.randint(0.0,1.0) for i in range(0,3)])
b=[[i] for i in range(0,3)]
#b=b.transpose()
b=np.array(b)
'''
def RElu(a):
    ar=[]
    for v in a:
        ar.append([1 if v>0.5 else 0])

    return ar


'''a=np.array([random.randint(0.0,1.0) for i in range(2)]).reshape(2,2)
b=np.array([random.randint(0.0,1.0) for i in range(2)]).reshape(2,2)##a=a.transpose'''
'''a=np.array([[1,2]])
print(a)
x=a.transpose()
print(x)
print(np.dot(a,x))'''
