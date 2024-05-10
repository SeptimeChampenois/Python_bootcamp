def my_levenshtein(string1, string2):
    distance_between = 0
    if len(string1) != len(string2):
        return -1
    else:
        for i in range(len(string1)):
            if string1[i] == string2[i]:
                distance_entre += 1
    return distance_between


example = my_levenshtein("GGACTGA", "GGACTGA")
print(example)
