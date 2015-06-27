#!/usr/bin/env python3

import math

def op_and(a,b):
	if a == 1 and b == 1:
		return 1
	else:
		return 0
		
def op_or(a,b):
	if a == 1 or b == 1:
		return 1
	else:
		return 0
		
def op_inv(a):
	if a == 1:
		return 0
	else:
		return 1

def r_sum(a,b):
	return op_and(op_or(a,b), op_inv(op_and(a, b)))
	
list_d = []

for i in range(1,3):
	d_input = float(input ("Enter d_input({}): ".format(i)))

	c_of_bit = math.ceil(math.log(d_input,2))

	d_string = ''
	n = c_of_bit
	d = 2**n

	if d_input >= d:
		d_string = d_string + '1'
	
	d_input = math.fmod(d_input, d)
	n = n - 1
	while n >= 0:

		d = 2**n
	
		if d_input < d:
			d_string = d_string + '0'
		else:
			d_string = d_string + '1'
		
		d_input = math.fmod(d_input, d)
		n = n - 1
		
	list_d.append(d_string)

tmp_1 = ''
tmp_2 = ''
		
if len(list_d[0]) > len(list_d[1]):
	dif_len = len(list_d[0]) - len(list_d[1])
	while dif_len > 0:
		tmp_2 = tmp_2 + '0'
		dif_len = dif_len - 1
			
elif len(list_d[0]) < len(list_d[1]):
	dif_len = len(list_d[1]) - len(list_d[0])
	while dif_len > 0:
		tmp_1 = tmp_1 + '0'
		dif_len = dif_len - 1

tmp_1 = tmp_1 + list_d[0]
tmp_2 = tmp_2 + list_d[1]
str_result = ''
n = len(tmp_1)

print(" ", tmp_1)
print("+", tmp_2)
str_m = "  " + '-'*n
print(str_m)

n = len(tmp_1)
tmp_a = int(tmp_1[n - 1])
tmp_b = int(tmp_2[n - 1])

#first half-adder
S = r_sum(tmp_a, tmp_b)
CO = op_and(tmp_a, tmp_b)

str_result = str_result + str(S)
n = n - 1
tpm_CO = 0
while n > 0:
	tmp_a = int(tmp_1[n - 1])
	tmp_b = int(tmp_2[n - 1])
	
	#first half-adder
	S = r_sum(tmp_a, tmp_b)
	tmp_CO = op_and(tmp_a, tmp_b)
	
	#second half-adder
	S = r_sum(S, CO)
	CO = op_and(S, CO)
	
	CO = op_or(CO, tmp_CO)
	if n != 1:
		str_result = str_result + str(S)
	else:
		str_result = str_result + str(S)
		str_result = str_result + str(CO)
	n = n - 1

str_result_out = str_result[::-1]

result = 0
n = len(str_result_out) - 1
for i in  str_result_out:
	result = result + int(i)*(2**n)
	n = n - 1

print(" ", str_result_out)
print ("Result = ", result)