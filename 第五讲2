import numpy as np

x=np.array([64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03])
y=np.array([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84])

xm=np.mean(x)
ym=np.mean(y)

x=x-xm
y=y-ym
zm=x*y
zs=x*x

w=np.sum(zm)/np.sum(zs)
b=ym-w*xm;
print("w=%f\tb=%f\t"%(w,b))
