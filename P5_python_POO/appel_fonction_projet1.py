import csv
from Projet1_1python import *
import sys 
from pprint import pprint
class valide_invalide:
    dict_valide = {}
    dict_invalide = {}
    dict_note_valide = {}
    dict_note_invalide = {}
    dict_moy_Generale = {}
    list_valides = []
    list_invalides = []
    list_note_valides = []
    list_note_invalides = []
    list_moy_Generale = []
    # j'ai instancié un objet de la classe lesFonctions
    lesfonction = lesFonctions()
    data = csv.reader(open("data.csv","r+"),delimiter =",")

    with open("data100code.csv","w") as datas:
        writer = csv.writer(datas)
        for line in data:
            writer.writerow((line[1],line[2],line[3],line[4],line[5],line[6]))
        

    # Maintenant on a un fichier sans le code         
    data100code = csv.reader(open("data100code.csv","r+"),delimiter =",")

    for line in data100code:
        # si numero valide return True sinon False
        numero = lesfonction.numeroValide(line[0])
        print(numero)
        # si nom valide return True sinon False
        nom = lesfonction.nomValide(line[1])
        # prenom return True si c'est valide sinon False
        prenom = lesfonction.prenomValide(line[2])
        notee = lesfonction.noteValide(line[5])  # noteValide return liste [] de note si c'est valide sinon False
        # changerFormatDate return date si c'est bon sinon False
        # dateValide return True si c'est valide sinon False
        date = lesfonction.changerFormatDate(line[3])
        if date == False:
            continue
        else:
            dateVal = lesfonction.dateValide(date)  
        classe = lesfonction.definirFormatClasse(line[4])  # definirFormatClasse return classe(valide) False (sinon)
        if classe == False:
            continue
        else:
            classeValid = lesfonction.classeValide(classe)  # classeValide return True (valide) False(sinon)    
        # if notee == False:
        #     continue
        # else:
        #     MoyGeneralEtud  = calculMoyenGeneral(notee)  
        # dict = {'Date de naissance':}

        if numero == True and nom == True and prenom == True and date != False and dateVal == True and classe != False and classeValid == True and notee != False:
            dict_valide ={"Numero":line[0],"Nom":line[1],"Prenom":line[2],"Date de naissance":date,"Classe":classe}
            dict_note_valide = {"Numero":line[0],"Note":notee}
            list_valides.append(dict_valide)
            list_note_valides.append(dict_note_valide)
        

        else:
            dict_invalide ={"Numero":line[0],"Nom":line[1],"Prenom":line[2],"Date de naissance":date,"Classe":classe}
            dict_note_invalide = {"Numero":line[0],"Note":notee}
            list_invalides.append(dict_invalide)
            list_note_invalides.append(dict_note_invalide) 

    for row in list_note_valides: 
        MoyGeneralEtud = lesfonction.calculMoyenGeneral(row["Note"])
        dict_moy_Generale = {"Numero":row["Numero"],"MoyenGeneral":MoyGeneralEtud}
        list_moy_Generale.append(dict_moy_Generale)
        dict_moy_Generale={}
    dict_moy_croissant = sorted(dict_moy_Generale , key=lambda d:d['MoyenGeneral'],reverse = True)
    print(50*"°")
    # for lin in dict_moy_croissant:
        # print(lin)
            
    """ **********************************************************  """
                # Voici la partie Menu du projet
    """ **********************************************************  """    

    menu = 1

    while menu in [1,2,3,4,5]:
        print(50*"")
        print(10*" ","Voici le Menu: \n 1• Afficher les informations\n 2•Afficher une information par son Numero\n 3•afficher les cinq premiers par leur moyenne \n 4• Ajouter une Information \n 5• Modifier une information Invalide\n 6•Pour Quitter")
        print(50*"")
        menu = int(input())
        if menu == 1:
            sous_menu = int(input("choisir entre données valide ou invalide\n 1• Afficher les informations Valides \n 2• Afficher les informations Invalides\n"))
            if sous_menu == 1:
                lesfonction.afficherInfoValides(list_valides)
                lesfonction.afficherNoteValide(list_note_valides)
            elif sous_menu == 2:
                print("methode affichage invalide")
                lesfonction.afficherInfoValides(list_invalides) 
                lesfonction.afficherNoteValide(list_note_invalides)
        elif menu == 2:
            numero =input("Entrer votre numero svp")
            lesfonction.afficherUneInfo(numero,list_valides,list_invalides,list_note_valides,list_note_invalides)
        elif menu == 3:
            print("En cours de traitement")   
        elif menu == 4:
            lesfonction.ajouterInfo() 
        elif menu == 5:
            print("En cours de traitement")
        else:
            exit  






