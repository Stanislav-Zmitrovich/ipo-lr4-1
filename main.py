# Запрашиваем число
number = int(input("Введите число: "))
# Выводим четные числа от 0
print("Четные числа от 0 до",number,":")
for i in range(0, number + 1, 2):
 print(i, end=" ")
