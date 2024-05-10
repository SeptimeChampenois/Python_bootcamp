def my_is_sort(arr):
    if len(arr) == 0:
        return True
    if arr == sorted(arr,reverse=False):
        return True
    elif arr == sorted(arr,reverse=True):
        return True
    else:
        return False



def my_is_sort(arr):
    # list empty or not
    if len(arr) == 0:
        return True

    # Vérifie si la liste est triée dans l'ordre croissant
    sorted_asc = True
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            sorted_asc = False
            break

    if sorted_asc:
        return True

    # Vérifie si la liste est triée dans l'ordre décroissant
    sorted_desc = True
    for i in range(1, len(arr)):
        if arr[i - 1] < arr[i]:
            sorted_desc = False
            break

    if sorted_desc:
        return True

    # Si la liste n'est pas triée dans l'ordre croissant ou décroissant,
    # alors elle n'est pas triée du tout, donc retourne False
    return False

# Tests de la fonction
print(my_is_sort([10, 4, 5, 8, 10]))
