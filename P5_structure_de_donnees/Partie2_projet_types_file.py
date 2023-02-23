import csv
import json
from Projet1_1python import *
# ecrire dans un fichier json
data_csv = csv.DictReader(open('data100code.csv'),delimiter = ',')
json_array=[]
for line in data_csv:
    json_array.append(line)

with open('data100code.json','w') as file:
        jsonString = json.dumps(json_array,indent=4)
        file.write(jsonString)

data_json = open('data100code.json','r')
data_lire = json.load(data_json)



# ecrire dans un fichier xml
list_data_csv = csv.reader(open("data100code.csv"))     
xml_array = []
for row in list_data_csv:
    xml_array.append(row)
#print(data[1:])
def convert_row_csv_en_xml(row):
    return """
    <Eleve>
        <Numero> %s </Numero>
        <Nom> %s </Nom>
        <Prenom> %s </Prenom>
        <Date_de_naissance> %s </Date_de_naissance>
        <Classe> %s </Classe>
        <Note> %s </Note> 
        
    </Eleve>  """ %(row[0],row[1],row[2],row[3],row[4],row[5])
with open("data100code.xml","w") as f:
    f.write("<?xml version = '1.0' encoding ='ISO-8859-1' standalone ='no' ?>\n <Eleves>")
    f.write("\n".join([convert_row_csv_en_xml(row) for row in xml_array[1:]])) 
    f.write("\n </Eleves>")   
    

# si l'utilisateur a choisi de travailler avec json

liste_Valide_tmp = ["Numero","Nom","Prenom","Date de Naissance","Classe","Note"]
liste_valide_finale = []
liste_valide_finale.append(liste_Valide_tmp)
xml_data="" 
for line in data_lire:
    # si numero valide return True sinon False
    numero = numeroValide(line["Numero"])
    # si nom valide return True sinon False
    nom = nomValide(line["Nom"])
    # prenom return True si c'est valide sinon False
    prenom = prenomValide(line["Prénom"])
    notee = noteValide(line["Note"])  # noteValide return liste [] de note si c'est valide sinon False
    # changerFormatDate return date si c'est bon sinon False
    # dateValide return True si c'est valide sinon False
    date = changerFormatDate(line["Date de naissance"])
    if date == False:
        continue
    else:
        dateVal = dateValide(date)  
    classe = definirFormatClasse(line["Classe"])  # definirFormatClasse return classe(valide) False (sinon)
    if classe == False:
        continue
    else:
        classeValid = classeValide(classe)  # classeValide return True (valide) False(sinon)   
    # si toutes les condition sont vraies on l'ajoute dans un ficher csv else on l'ajoute dans un fichier xml
    if numero == True and nom == True and prenom == True and date != False and dateVal == True and classe != False and classeValid == True and notee != False:      
        liste_Valide_tmp.append(line["Numero"])
        liste_Valide_tmp.append(line["Nom"])
        liste_Valide_tmp.append(line["Prénom"])
        liste_Valide_tmp.append(date)
        liste_Valide_tmp.append(classe)
        liste_Valide_tmp.append(notee)
        liste_valide_finale.append(liste_Valide_tmp)


    else:
        xml_data+=("""
        <Eleve>
            <Numero> %s </Numero>
            <Nom> %s </Nom>
            <Prenom> %s </Prenom>
            <Date_de_naissance> %s </Date_de_naissance>
            <Classe> %s </Classe>
            <Note> %s </Note> 
        </Eleve>  
        """ %(line["Numero"],line["Nom"],line["Prénom"],date,classe,notee))                 

with open("invalideData.xml","w+") as f:
    f.write("<?xml version = '1.0' encoding ='ISO-8859-1' standalone ='no' ?>\n <Eleves>")  
    f.write(xml_data)
    f.write("\n </Eleves>") 

for line in liste_valide_finale:
    print(line)