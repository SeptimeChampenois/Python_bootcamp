import datetime

#Convertir l'âge en chaîne de caractères

def transform_age(age):
    if age <= 20:
        return "->20"
    elif age <= 40:
        return "21->40"
    elif age <= 65:
        return "41->65"
    else:
        return "66->99"

#Convertir l'email en domaine

def transform_email(email):
    domain = email.split('@')[1]
    if domain == "yahoo.com":
        return "yahoo.com"
    elif domain == "hotmail.com":
        return "hotmail.com"
    else:
        return domain

#Extraire l'heure de la commande
def transform_order_at(datetime):
    hour = datetime.split(" ")[1].split(":")[0]
    hour = int(hour)
    if 6 <= hour <= 11:
        return "morning"
    elif 12 <= hour <= 17:
        return "afternoon"
    elif 18 <= hour <= 23:
        return "evening"

# Transformer les données

def my_data_transform(csv_content):
    transformed_data = []
    lines = csv_content.split("\n")

    # En-tête
    transformed_data.append(lines[0])

    # Lignes de données
    for line in lines[1:]:
        values = line.split(",")
        values[4] = transform_email(values[4])
        values[5] = transform_age(int(values[5]))
        values[9] = transform_order_at(values[9])
        transformed_data.append(",".join(values))

    return transformed_data

# Données CSV d'exemple
csv_content = "Gender,FirstName,LastName,UserName,Email,Age,City,Device,Coffee Quantity,Order At\nMale,Carl,Wilderman,carl,wilderman_carl@yahoo.com,29,Seattle,Safari iPhone,2,2020-03-06 16:37:56\nMale,Marvin,Lind,marvin,marvin_lind@hotmail.com,77,Detroit,Chrome Android,2,2020-03-02 13:55:51\nFemale,Shanelle,Marquardt,shanelle,marquardt.shanelle@hotmail.com,21,Las Vegas,Chrome,1,2020-03-05 17:53:05\nFemale,Lavonne,Romaguera,lavonne,romaguera.lavonne@yahoo.com,81,Seattle,Chrome,2,2020-03-04 10:33:53\nMale,Derick,McLaughlin,derick,mclaughlin.derick@hotmail.com,47,Chicago,Chrome Android,1,2020-03-05 15:19:48\n"

# Transformer les données CSV
transformed_data = my_data_transform(csv_content)
print(transformed_data)
