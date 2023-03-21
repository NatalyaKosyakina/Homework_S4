# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

num_n = int(input("Число n: "))
num_m = int(input("Число m: "))

list_n = input("Укажите числа набора N через пробел: ").split(" ")
list_n = list(filter(None, list_n))
if len(list_n) > num_n :
    list_n = list_n[:num_n]

list_m = input("Укажите числа набора M через пробел: ").split(" ")
list_m = list(filter(None, list_m))
if len(list_m) > num_m :
    list_m = list_m[:num_m]

for i in range(len(list_n)):
    list_n[i] = int(list_n[i])
for i in range(len(list_m)): 
    list_m[i] = int(list_m[i])

set_n, set_m = set(list_n), set(list_m)
result = list((set_n.intersection(set_m)))
result.sort()
print(result)