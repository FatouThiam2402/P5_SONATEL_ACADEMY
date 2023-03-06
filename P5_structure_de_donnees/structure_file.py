from Partie2_projet_types_file import *

def choixFileValideInvalide():
    print("***Veuillez choisir le type de fichier en Output*** ")
    valide = int(input("\t\t*** Valide ***\n \n\t\t  1• CSV \n \t\t 2• JSON \n\t\t  3• XML\n "))
    invalide = int(input("\t\t*** InValide *** \n \t\t 1• CSV \n\t\t 2• JSON \n\t\t 3• XML\n"))
    return valide,invalide


choix = int(input("\t\t***Veuillez choisir le type de fichier en input***  \n\t\t 1• CSV \n\t\t 2• JSON \n\t\t 3• XML\n"))
if choix == 1:
    data100code = csv.reader(open("data100code.csv","r")) 
    liste_valide,liste_invalide = input_csv(data100code)
    valide,invalide = choixFileValideInvalide()
    if valide == 1:
        valide_en_csv(liste_valide)
    elif valide == 2:
        valide_en_json(liste_valide)
    elif valide == 3:
        valide_en_xml(liste_valide)
    if invalide == 1:
        invalide_en_csv(liste_invalide)
    elif invalide == 2:    
        invalide_en_json(liste_invalide)
    elif invalide == 3:    
        invalide_en_xml(liste_invalide)

elif choix == 2:
    data_json = open('data100code.json','r')    
    data_lire = json.load(data_json)
    liste_valide,liste_invalide = input_file_json(data_lire)
    valide,invalide = choixFileValideInvalide()
    if valide == 1:
        valide_en_csv(liste_valide)
    elif valide == 2:
        valide_en_json(liste_valide)
    elif valide == 3:
        valide_en_xml(liste_valide)
    if invalide == 1:
        invalide_en_csv(liste_invalide)
    elif invalide == 2:    
        invalide_en_json(liste_invalide)
    elif invalide == 3:    
        invalide_en_xml(liste_invalide)

elif choix == 3:
    liste_dict = []
    data_xml = open("data100code.xml","r") 
    # liste_valide,liste_invalide = input_file_xml(data_xml) # erreur à revoir

    # valide,invalide = choixFileValideInvalide()
    # if valide == 1:
    #     valide_en_csv(liste_valide)
    # elif valide == 2:
    #     valide_en_json(liste_valide)
    # elif valide == 3:
    #     valide_en_xml(liste_valide)
    # if invalide == 1:
    #     invalide_en_csv(liste_invalide)
    # elif invalide == 2:    
    #     invalide_en_json(liste_invalide)
    # elif invalide == 3:    
    #     invalide_en_xml(liste_invalide)

  
