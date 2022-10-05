n = int(input("Введите число: "))
lst= [i for i in range(-n, n+1)]
print(lst)
for j in lst:
    for z in lst:
        if lst[j] == lst[z]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print(lst)