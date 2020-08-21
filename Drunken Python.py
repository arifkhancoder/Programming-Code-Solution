#ord() and char() details : https://realpython.com/python-strings/
#Edabit (medium)
#Solved By Md Ariful Islam

def str_to_int(num_str):
	num = 0
	for char in num_str:
		num *= 10
		num += ord(char) - ord('0')
	return num

def int_to_str(num_int):
	word = ""
	while num_int:
		word = chr(ord('0') + num_int % 10) + word
		num_int //= 10
	return word or "0"
