a=str(input("Enter the name of the file "))
f1=open(a,'r')
l=f1.readline()
n=1
sum = 0
while(l!=""):
    n=n+1
    sum=sum+int(1)
    l=f1.readline()
print('Average is',end='')
print(sum/(n-1))
f1.close()
