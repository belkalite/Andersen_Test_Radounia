numbers =[]
print ('Введите целые числа, разделяя пробелами')
numbers = list(map(int, input().split()))
print ('Элементы, кратные 3:')
for i in numbers:
	if i%3 == 0:
		print (i)
input('Нажмите Enter для выхода')
