import tensorflow as tf
import matplotlib.pyplot as plt
husing=tf.keras.datasets.boston_housing
(train_x,train_y),(test_x,test_y)=husing.load_data(test_split=0)

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

titles=["CRIM","ZN","INDUS","CHAS","NOX","RM","AGE","DIS","RAD","TAX","PTRATIO","B","LSTAT"]

print("1 -- CRIM\n2 -- ZN\n3 -- INDUS\n4 -- CHAS\n5 -- NOX\n6 -- RM\n7 -- AGE\n8 -- DIS\n9 -- RAD\n10 -- TAX\n11 -- PTRATIO\n12 -- B\n13 -- LSTAT\n")
a=int(input("请选择属性："))
plt.figure(figsize=(5,5))
plt.scatter(train_x[:,a],train_y)
plt.xlabel(titles[a])
plt.ylabel("Price($100's)")
plt.title(str(a)+"."+titles[a-1]+" - Price")
plt.tight_layout()
plt.show()
