def my_csv_parser(string, separator):
    lines = string.split("\n")
    csv_parser_array = []

    i = 0
    while i < len(lines):
        values = lines[i].split(separator)
        csv_parser_array.append(values)
        i += 1

    return csv_parser_array

# Exemples de données CSV et de séparateurs à tester
data1 = "a,b,c\n1,2,3\n4,5,6"
data2 = "1|2|3\n4|5|6"
separator1 = ","
separator2 = "|"

# Tester la fonction avec les données et les séparateurs spécifiés
result1 = my_csv_parser(data1, separator1)
result2 = my_csv_parser(data2, separator2)

# Afficher les résultats
print("Résultat avec séparateur , :", result1)
print("Résultat avec séparateur | :", result2)
