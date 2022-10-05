n = int(input("Введите число: "))
lst= [i for i in range(-n, n+1)]
print(lst)
index1 = int(input("Введите число: "))
index2 = int(input("Введите число: "))
for j in lst:
        if j == index1:
                for z in lst:
                        if z == index2:
                                h = lst[j]*lst[z]
                                print(h)
