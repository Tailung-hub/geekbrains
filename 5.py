# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

with open("num_list.txt", "w", encoding="utf_8") as f:
    x = 0
    while x != 10:
        f.write(str(randint(0, 100)) + " ")
        x += 1
with open("num_list.txt", "r") as z:
    nums = z.read().split()
    print("Список чисел: ", nums)
    sum_nums = 0
    for i in nums:
        i = int(i)
        sum_nums += i
    print("Сумма =", sum_nums)
