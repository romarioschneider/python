list_size = []
list_size_sort = []

f = open('data.txt')

for i in range(0, 3):
    line = f.readline()
    if i == 0:
        customer_size = int(line)
    elif i == 1:
        count_shoes = int(line)
    else:
        j = 0
        h = 0
        n = ''
        for n in line:
            if n != " ":
                j = j + 1
            else:
                list_size.append(int((line[h:j])))
                j = j + 1
                h = j
        list_size.append(int(line[h:len(line)].replace('\n', '')))
        
#if len(list_size) != count_shoes:
#    print('Wrong input data!')
#    exit(1)
    
list_size_sort = sorted(list_size)

i = 0
h = 0
while i != len(list_size_sort):
    if list_size_sort[i] >= customer_size:
        n = list_size_sort[i]
        j = i
        h = h + 1
        break
    else:
        i = i + 1
        
if h == 0:
    exit(1)
else:
    i = j + 1
    while i != len(list_size_sort):
        if list_size_sort[i] > (n + 3):
            h = h + 1
            n = list_size_sort[i]
            i = i + 1
        else:
            i = i + 1
      
print(h)
#print(customer_size)
#print(count_shoes)
#print(list_size)
#print(list_size_sort)
