import math
a=int(input(""))
b=int(input(""))
c=int(input(""))
de = b*b-4*a*c
if de== 0:
   x=-b/(2*a)
   print(x)     
elif de > 0:
   x1 =(-b-math.sqrt(de))/(2*a)
   x2 =(-b+math.sqrt(de))/(2*a)
   print("%d %d"%(x1,x2))            
else:
   print("此方程无解")
