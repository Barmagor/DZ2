from asyncore import write
#1 способ
n = int(input("Введите число: "))
lst= [i for i in range(-n, n+1)]
print(lst)
c=1
ind1=open("file1.txt", "r")
a=ind1.readlines()
for i in a:
        u=int(i.strip())
        print(u)
        c=lst[u]*c
print(c)
#2 способ
n = int(input("Введите число: "))
lst= [i for i in range(-n, n+1)]
print(lst)
b=1
ind1=open("file1.txt", "r")
while True:
        a=ind1.readline()
        if a =="":
                break
        a=int(a.strip())
        b=lst[a]*b
print(b)
