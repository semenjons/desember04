#  Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

from random import randint as rd  
k = int(input('Введите K: ')) 
for i in range(k, 0, -1):
         x = rd(-100, 100)
         if x > 0:
            print(f"+{x}x^{i}", end=' ')
         else:         
             print(f"{x}x^{i}", end=' ')
print(rd(-100,100), end='')

# я не успеваю во всем разбираться, делаю что могу. 
