def my_isalpha(param_1):
    if 'A' <= param_1 <= 'Z' or 'a' <= param_1 <= 'z':
        return 1
    return 0

print(my_isalpha('A')) 
print(my_isalpha('z'))  
print(my_isalpha('5'))  

def my_isalpha(param_1):
	letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
	for i in letters:
		if i == param_1:
			return 1
	else:
		return 0

print(my_isalpha("A"))
