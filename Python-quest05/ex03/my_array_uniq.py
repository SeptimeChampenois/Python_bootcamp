def my_array_uniq(param_1):
    x = []
    for i in param_1:
        if i not in x:
            x.append(i)
    return x

#function test
#result = my_array_uniq([1, 2, 2, 3, 4, 4, 5])
#print(result)


def my_array_uniq(param_1):
    x = []  
    count = 0 
    for i in param_1:
        found = False 
        for j in x:
            if i == j:
                found = True 
                break
        if not found:
            x.append(i) 
            count += 1 

    return x  

# function test
result = my_array_uniq([1, 2, 2, 3, 4, 4, 5])
print("Résultat :", result)
