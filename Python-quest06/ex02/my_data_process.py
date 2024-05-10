import json

def add_values(result, key, value):
    if key not in result:
        result[key] = {value: 0}
    elif value not in result[key]:
        result[key][value] = 0
    result[key][value] += 1

def my_data_process(csv_content):
    my_data_processed = {
        "Gender": {},
        "Email": {},
        "Age": {},
        "City": {},
        "Device": {},
        "Order At": {}
    }

    lines = csv_content[1:]  # Ignorer l'en-tête
    for line in lines:
        values = line.split(',')
        add_values(my_data_processed, "Gender", values[0])
        add_values(my_data_processed, "Email", values[4])
        add_values(my_data_processed, "Age", values[5])
        add_values(my_data_processed, "City", values[6])
        add_values(my_data_processed, "Device", values[7])
        add_values(my_data_processed, "Order At", values[9])

    return json.dumps(my_data_processed)

# Données CSV d'exemple
csv_content = [
    "Gender,FirstName,LastName,UserName,Email,Age,City,Device,Coffee Quantity,Order At",
    "Male,Carl,Wilderman,carl,wilderman_carl@yahoo.com,29,Seattle,Safari iPhone,2,2020-03-06 16:37:56",
    "Male,Marvin,Lind,marvin,marvin_lind@hotmail.com,77,Detroit,Chrome Android,2,2020-03-02 13:55:51",
    "Female,Shanelle,Marquardt,shanelle,marquardt.shanelle@hotmail.com,21,Las Vegas,Chrome,1,2020-03-05 17:53:05",
    "Female,Lavonne,Romaguera,lavonne,romaguera.lavonne@yahoo.com,81,Seattle,Chrome,2,2020-03-04 10:33:53",
    "Male,Derick,McLaughlin,derick,mclaughlin.derick@hotmail.com,47,Chicago,Chrome Android,1,2020-03-05 15:19:48"
]

# Traitement des données CSV
result = my_data_process(csv_content)
print(result)
