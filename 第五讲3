import numpy as np

x0=np.ones(10) 
x1=np.array([64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03])
x2=np.array([2,3,4,2,3,4,2,4,1,3])
y=np.array([62.55,82.42,132.62,73.31,131.05,86.57,84.49,127.44,55.25,104.84])

x=np.vstack((x0,x1,x2))
x=x.T
y=y.reshape(y.shape[0],1)
w=np.matrix(np.dot(x.T,x))*np.dot(x.T,y)
print(w.shape)
print("---------------")
print(x)
print("---------------")
print(y)
print("---------------")
print(w)
