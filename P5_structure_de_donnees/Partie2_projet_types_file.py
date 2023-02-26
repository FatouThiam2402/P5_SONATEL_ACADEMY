import csv
import json
from Projet1_1python import *
from lxml import etree
from pprint import pprint 
from sys import exit 

data = csv.reader(open("data.csv","r+"),delimiter =",")
with open("data100code.csv","w") as datas:
    writer = csv.writer(datas)
    for line in data:
        writer.writerow((line[1],line[2],line[3],line[4],line[5],line[6]))

# convertir le fichier global de csv en json
data_csv = csv.DictReader(open('data100code.csv'),delimiter = ',')
json_array=[]
for line in data_csv:
    json_array.append(line)

with open('data100code.json','w') as file:
        jsonString = json.dumps(json_array,indent=4)
        file.write(jsonString)

data_json = open('data100code.json','r')# a enlever
data_lire = json.load(data_json)

# convertir le fichier global de csv en xml
list_data_csv = csv.reader(open("data100code.csv"))     
xml_array = []
for row in list_data_csv:
    xml_array.append(row)
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
    
# fonction qui prend en entrer le fichier de base json   et retourne deux listes(valide et invalide)
def input_file_json(file_json):
    liste_Valide_tmp = []
    liste_invalide_tmp = []
    liste_valide_finale = []
    liste_invalide_finale = []
    for line in file_json:
        numero = numeroValide(line["Numero"])
        nom = nomValide(line["Nom"])
        prenom = prenomValide(line["Prénom"])
        notee = noteValide(line["Note"])
        date = changerFormatDate(line["Date de naissance"])
        if date == False:
            continue
        else:
            dateVal = dateValide(date)  
        classe = definirFormatClasse(line["Classe"])
        if classe == False:
            continue
        else:
            classeValid = classeValide(classe)  
        if numero == True and nom == True and prenom == True and date != False and dateVal == True and classe != False and classeValid == True and notee != False:      
            liste_Valide_tmp.append(line["Numero"])
            liste_Valide_tmp.append(line["Nom"])
            liste_Valide_tmp.append(line["Prénom"])
            liste_Valide_tmp.append(date)
            liste_Valide_tmp.append(classe)
            liste_Valide_tmp.append(notee)
            liste_valide_finale.append(liste_Valide_tmp)
        else:
            liste_invalide_tmp.append(line["Numero"])
            liste_invalide_tmp.append(line["Nom"])
            liste_invalide_tmp.append(line["Prénom"])
            liste_invalide_tmp.append(date)
            liste_invalide_tmp.append(classe)
            liste_invalide_tmp.append(notee)
            liste_invalide_finale.append(liste_invalide_tmp)

    return liste_valide_finale,liste_invalide_finale 
  


  

# for line in liste_invalide_finale:
#         xml_data = ""
#         xml_data+=("""
#         <Eleve>
#             <Numero> %s </Numero>
#             <Nom> %s </Nom>
#             <Prenom> %s </Prenom>
#             <Date_de_naissance> %s </Date_de_naissance>
#             <Classe> %s </Classe>
#             <Note> %s </Note> 
#         </Eleve>  
#         """ %(line[0],line[1],line[2],line[3],line[4],line[5]))                 

# with open("invalideData.xml","w+") as f:
#     f.write("<?xml version = '1.0' encoding ='ISO-8859-1' standalone ='no' ?>\n <Eleves>")  
#     f.write(xml_data)
#     f.write("\n </Eleves>") 
#****************************************************")
# fonction qui prend en entrer le fichier de base xml   et retourne deux listes(valide et invalide)
def input_file_xml(file_xml):
    liste_dict = []
    my_tree = etree.parse(file_xml)

    for num,nom,prenom,naiss,classe,note in my_tree.xpath("/Eleves/Eleve"):
        liste_dict.append({
            'Numero' : num.text,
            'Nom' : nom.text,
            'Prénom' : prenom.text,
            'Date de naissance' : naiss.text,
            'Classe' : classe.text,
            'Note' : note.text, 
        })
    return liste_dict

#### Probleme
# liste_dict = []    
# data_xml = open("data100code.xml","r") 
# liste_dict = input_file_xml(data_xml)

# print(10*"*")
# pprint(liste_dict)

# liste_Valide_tmp = []
# liste_invalide_tmp = []
# liste_valide_finale = []
# liste_invalide_finale = []

# for line in liste_dict:
#     numero = numeroValide(line["Numero"])
#     nom = nomValide(line["Nom"])
#     prenom = prenomValide(line["Prénom"])
#     notee = noteValide(line["Note"])  
#     date = changerFormatDate(line["Date de naissance"])
#     if date == False:
#         continue
#     else:
#         dateVal = dateValide(date)  
#     classe = definirFormatClasse(line["Classe"]) 
#     if classe == False:
#         continue
#     else:
#         classeValid = classeValide(classe)  
#     if numero == True and nom == True and prenom == True and date != False and dateVal == True and classe != False and classeValid == True and notee != False:      
#         liste_Valide_tmp.append(line["Numero"])
#         liste_Valide_tmp.append(line["Nom"])
#         liste_Valide_tmp.append(line["Prénom"])
#         liste_Valide_tmp.append(date)
#         liste_Valide_tmp.append(classe)
#         liste_Valide_tmp.append(notee)
#         liste_valide_finale.append(liste_Valide_tmp)
        
#     else:
#         liste_invalide_tmp.append(line["Numero"])
#         liste_invalide_tmp.append(line["Nom"])
#         liste_invalide_tmp.append(line["Prénom"])
#         liste_invalide_tmp.append(date)
#         liste_invalide_tmp.append(classe)
#         liste_invalide_tmp.append(notee)
#         liste_invalide_finale.append(liste_invalide_tmp)
#         for row in liste_invalide_finale:
#             print(row) 
#****************************************************
# fonction qui prend en entrer le fichier de base csv   et retourne deux listes(valide et invalide)

def input_csv(data100code):
    list_valides =[]
    list_invalides = []
    for line in data100code:
        numero = numeroValide(line[0])
        nom = nomValide(line[1])
        prenom = prenomValide(line[2])
        notee = noteValide(line[5]) 
        date = changerFormatDate(line[3])
        if date == False:
            continue
        else:
            dateVal = dateValide(date)  
        classe = definirFormatClasse(line[4])  
        if classe == False:
            continue
        else:
            classeValid = classeValide(classe)    
        if numero == True and nom == True and prenom == True and date != False and dateVal == True and classe != False and classeValid == True and notee != False:
            list_valides.append(line)
        else:
            list_invalides.append(line)

    return list_valides,list_invalides 

# fonction qui écrit les données valides dans un fichier xml
def valide_en_xml(liste_valide):
    xml_data = ""
    for line in liste_valide:
        xml_data+=("""
        <Eleve>
            <Numero> %s </Numero>
            <Nom> %s </Nom>
            <Prenom> %s </Prenom>
            <Date_de_naissance> %s </Date_de_naissance>
            <Classe> %s </Classe>
            <Note> %s </Note> 
        </Eleve>  
        """ %(line[0],line[1],line[2],line[3],line[4],line[5]))                 
    with open("valideData.xml","w+") as f:
        f.write("<?xml version = '1.0' encoding ='ISO-8859-1' standalone ='no' ?>\n <Eleves>")  
        f.write(xml_data)
        f.write("\n </Eleves>") 

        
# fonction qui écrit les données invalides dans un fichier xml

def invalide_en_xml(liste_invalide):
    xml_data = ""
    for line in liste_invalide:
        xml_data+=("""
        <Eleve>
            <Numero> %s </Numero>
            <Nom> %s </Nom>
            <Prenom> %s </Prenom>
            <Date_de_naissance> %s </Date_de_naissance>
            <Classe> %s </Classe>
            <Note> %s </Note> 
        </Eleve>  
        """ %(line[0],line[1],line[2],line[3],line[4],line[5]))                 

    with open("InvalideData.xml","w+") as f:
        f.write("<?xml version = '1.0' encoding ='ISO-8859-1' standalone ='no' ?>\n <Eleves>")  
        f.write(xml_data)
        f.write("\n </Eleves>") 

# fonction qui écrit les données invalides dans un fichier json

def invalide_en_json(liste_invalide):
    liste_dict_invalide = []
    for line in liste_invalide:
        dict_invalide ={
            "Numero":line[0],
            "Nom":line[1],
            "Prenom":line[2],
            "Date de naissance":line[3],
            "Classe":line[4],
            "Note":line[5]
            }
        liste_dict_invalide.append(dict_invalide)
    with open('invalideData.json','w') as file:
        jsonString = json.dumps(liste_dict_invalide,indent=4)
        file.write(jsonString)    

# fonction qui écrit les données valides dans un fichier json

def valide_en_json(liste_valide):
    liste_dict_valide = []
    for line in liste_valide:
        dict_valide ={
            "Numero": line[0],
            "Nom": line[1],
            "Prenom": line[2],
            "Date de naissance": line[3],
            "Classe": line[4],
            "Note": line[5]
            }
        liste_dict_valide.append(dict_valide)
    with open('valideData.json','w') as file:
        jsonString = json.dumps(liste_dict_valide,indent=4)
        file.write(jsonString)   

# fonction qui écrit les données valides dans un fichier csv
def valide_en_csv(liste_valide):
    headers = ["Numero","Nom","Prenom","Date de Naissance","Classe","Note"]
    with open("valideData.csv","w") as file:
        w = csv.DictWriter(file,fieldnames=headers,delimiter=';')
        w.writeheader()
        for row in liste_valide:
            w.writerow({headers[0]:row[0],headers[1]:row[1],headers[2]:row[2],headers[3]:changerFormatDate(row[3]),headers[4]:definirFormatClasse(row[4]),headers[5]:row[5]})  

    file.close()

# fonction qui écrit  les donnees invalides dans un fichier  CSV
def invalide_en_csv(liste_invalide):
    headers = ["Numero","Nom","Prenom","Date de Naissance","Classe","Note"]
    with open("invalideData.csv","w") as file:
        w = csv.DictWriter(file,fieldnames=headers,delimiter=';')
        w.writeheader()
        for row in liste_invalide:
            w.writerow({headers[0]:row[0],headers[1]:row[1],headers[2]:row[2],headers[3]:changerFormatDate(row[3]),headers[4]:definirFormatClasse(row[4]),headers[5]:row[5]})  

    file.close()  
        








    



