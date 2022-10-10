n = float(input("Введите число: "))
count=0
g=str(n)
h=list(g)
j=0
for j in h:
    if "." not in j:
        count+=1
    elif "." in j:
        count=0
print(count)
num=n*pow(10, count)
int(num)
print(num)
sum = 0
while (num != 0):
    sum = sum + num % 10
    num = num // 10
print("Сумма цифр: ", sum)