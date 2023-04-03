##using while loop for printing table 03/04/2023
num = int(input("Enter a Number:\t"))

i=1
while i<=10:
    print(num,"x",i,"=",i*num)
    i+=1
print("End of loop!")

print('<','-' * 45,'>')

print("\n")
print("for list")
list1 = [11,15,18,"python",True,12,77]
for i in list1:
    print(i)
print("\n")

print("for tuple")
list2 = (12,45,88,"hello")
for i in list2:
    print(i)
print("\n")

print("for set")
list3 = {45,56,78,"abc"}
for i in list3:
    print(i)
print("\n")

list4 = "45,56,78,abc"
for i in list4:
    print(i)
print("\n")

##while in else
num = int(input("Enter a Number:\t"))

i=1
while i<=10:
    print(num,"x",i,"=",i*num)
    i+=1
else:
    print("End of loop!")

list1 = [11,15,18,"python",True,12,77]
for i in list1:
    print(i)
else:
    print("done!")

print('<','-' * 45,'>')

#wap to multiply all the given number of a list by 3

l1 = [11,15,18,12,77]
for i in l1:
    print(i*3)

l2 = ["Rajnish","Ishak","Nidhi","Vraj","Mansi","Akansha"]
for i in l2:
    print("hello",i)

l3 = ["Rajnish","Ishak","Nidhi","Vraj","Mansi","Akansha"]
for i in l3:
    print(i*3)

##
print("\n")
for i in range(10):
    print(i)

print("\n")
for i in range(44,100):
    print(i)

print("\n")
for i in range(44,99,7):
    print(i)

