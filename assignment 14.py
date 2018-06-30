

# q1
'''
f=open("test3.txt",encoding="utf8")
l=(f.readlines())
l.reverse()
n=int(input("enter the value of n"))
for i in range(0,n):
    print(l[i])
f.close()

'''
# q2

a="kill"
f=open("test3.txt","r")
k=f.read()
m=k.spilt()
print(k.count(a))

'''
# q 2
with open("test4.txt","w") as f:
    with open("test3.txt", "w") as f1:
            f1.write(f)
'''



# q4

with open("test4.txt","w") as f:
    with open("test3.txt", "w") as f1:
        for i in range(0,3):
            for line in f:
                for line in f1:
                    f1.write(f)











