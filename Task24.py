# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники, которая состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.


# Если достаточно найти только максимальное количество по всем кустам
bushes = input("Укажите количество ягод для каждого куста в грядке через пробел: ").split(" ")
bushes = list(filter(None, bushes))
max_berries = int(bushes[0])
for i in range(len(bushes)) :
    sum = int(bushes[i]) + int(bushes[i-1]) + int(bushes[i-2])
    if sum > max_berries :
        max_berries = sum
        best_position = i
print(f"За один заход можно собрать максимум {max_berries} ягод, при сброе с {best_position} куста.")