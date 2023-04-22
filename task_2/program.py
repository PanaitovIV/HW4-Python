# В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов. Эти кусты обладают разной урожайностью, 
# поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве 
# внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед 
# некоторым кустом заданной во входном файле грядки.

n = int(input('Введите количество кустов на грядке > '))
lst = []

print('Вводите последовательно число ягод на кустах > ')
for i in range(n):
    lst.append(int(input()))
    i += i
print(lst)

sum = []
for i in range(n):
    a = i
    b = i + 1
    c = i + 2
    if i == n-2:
        c = 0
    elif i == n-1:
        b = 0
        c = 1 
    sum.append(lst[a] + lst[b] + lst[c])
    i += i
print(f'Максимальное число ягод > {max(sum)}')