# 3. Задайте последовательность чисел. Напишите программу,
#  которая выведет список неповторяющихся элементов исходной последовательности.

lst = list(map(int, input('введите числа через пробел:\n').split()))
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(new_lst)
