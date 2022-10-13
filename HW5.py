import random
n = int(input("Введите число: "))
lst= [random.randint(0, 10) for i in range(-n, n+1)]
print(lst)
for j in range (len(lst)-1):
    for z in range(len(lst)-j-1):
        if lst[z] > lst[z+1]:
            lst[z], lst[z+1] = lst[z+1], lst[z]
print(lst)