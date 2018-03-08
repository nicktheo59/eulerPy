

number_str = '.'
number_len = 0
i = 1
while number_len < 1000500:
	number_str += str(i)
	i += 1
	number_len = len(number_str)

print int(number_str[1]) * int(number_str[10]) * int(number_str[100]) * int(number_str[1000]) * int(number_str[10000]) * int(number_str[100000]) * int(number_str[1000000]) 

