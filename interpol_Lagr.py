#!/usr/bin/env python3

print("--------------------Интерполяция по Лагранжу-----------------------")

chk = input("\nВведите 'file' для ввода значений из файла, 'test' - тестирование производительности или же 'Enter': ")
if chk == 'file':

	filename = input("Data-file: ")

	f = open(filename)

	list_line = []
	i = 0
	while i < 2:
		line = f.readline()
		if len(line) == 0:
			break
		else:
			list_line.append('')
			list_line[i] = line
		i = i + 1

#	i = 0
#	while i < 2:
#		print(list_line[i], end = '')
#		i = i + 1

	line_x = list_line[0] + ' '
	line_y = list_line[1] + ' '

	tmp = line_x.replace(',', '.')
	line_x = tmp.replace('\t', ' ')

	tmp = line_y.replace(',', '.')
	line_y = tmp.replace('\t', ' ')

	
	list_x = []
	list_y = []

	tmp = ''
	for i in line_x:
		if i != ' ':
			tmp = tmp + i
		else:
			list_x.append(float(tmp))
			tmp = ''
		
	tmp = ''
	for i in line_y:
		if i != ' ':
			tmp = tmp + i
		else:
			list_y.append(float(tmp))
			tmp = ''

elif chk == 'test':
#Блок, заполняющий массивы рандомными значениями (для тестирования быстродействия)

	line_x = ''
	line_y = ''
	import random
	n = int(input('count = '))

	i = 0
	while i < n:
		line_x = line_x + str(random.random() * 10) + ' '
		i = i + 1
	#print(line_x)
	i = 0
	while i < n:
		line_y = line_y + str(random.random() * 10) + ' '
		i = i + 1
	#print(line_y)


	list_x = []
	list_y = []

	tmp = ''
	for i in line_x:
		if i != ' ':
			tmp = tmp + i
		else:
			list_x.append(float(tmp))
			tmp = ''
		
	tmp = ''
	for i in line_y:
		if i != ' ':
			tmp = tmp + i
		else:
			list_y.append(float(tmp))
			tmp = ''


else:

	print("""После ввода всех значений Х введите "y" для начала ввода значений Y""", '\n') 
	i = 1
	list_x = [] # массив со значениями иксов
	while True:
		inp = input("X({}) = ".format(i)) 
		if inp != 'y': # для начала ввода значений y необходимо при вводе x ввести "y" - цикл ввода х прекращается
			list_x.append(float(inp))
			i = i + 1
		else:
			break

	list_y = [] # массив со значениями игриков
	ii = 1
	while ii < i:
		list_y.append(float(input("Y({}) = ".format(ii))))
		ii = ii + 1

print(list_x.__sizeof__())
print(list_y.__sizeof__())
print("\nРешение для набора узлов:")

n = len(list_x)
i = 0
while i < n:
	print("X({:0>3}) = {: f}   Y({:0>3}) = {: f}".format(i+1, list_x[i], i+1, list_y[i]))
	i = i + 1

x = float(input("X = "))

list_chis = []
i = 0
while i < n:
    ii = 0
#    print("iteration i = ", i)
    list_chis.append(1)
    while ii < n:
#        print("iteration ii = ", ii)
        if ii != i:
            list_chis[i] = list_chis[i] * (x - list_x[ii])
        ii = ii + 1
    i = i + 1

list_znam = []
i = 0
while i < n:
    ii = 0
#    print("iteration i = ", i)
    list_znam.append(1)
    while ii < n:
#        print("iteration ii = ", ii)
        if ii != i:
            list_znam[i] = list_znam[i] * (list_x[i] - list_x[ii])
        ii = ii + 1
    i = i + 1

i = 0
y = 0
while i < n:
    y = y + (list_chis[i] / list_znam[i] * list_y[i])
    i = i + 1

print("Результат: при Х = {} Y = {}".format(x, y))
