from Projet1_1python import *
# 1
# menu = 1

# while menu in [1,2,3,4,5]:
#     print(50*"")
#     print(10*" ","Voici le Menu: \n 1• Afficher les informations\n 2•Afficher une information par son Numero\n 3•afficher les cinq premiers par leur moyenne \n 4• Ajouter une Information \n 5• Modifier une information Invalide\n 6•Pour Quitter")
#     print(50*"")
#     menu = int(input())
#     if menu == 1:
#         sous_menu = int(input("choisir entre données valide ou invalide\n 1• Afficher les informations Valides \n 2• Afficher les informations Invalides\n"))
#         if sous_menu == 1:
#             print("methode affichage valide")
#         elif sous_menu == 2:
#             print("methode affichage invalide")    
#     elif menu == 2:
#         print("mehtode affichage info par son numero")
#     elif menu == 3:
#         print("methode affichage 5 premiers par leur moyenne")   
#     elif menu == 4:
#         print("methode ajouter une information")
#     elif menu == 5:
#         print("methode affichage modifier une information invalide")
#     else:
#         exit            

note1 = '#Math[10.5|15:15] #Francais[17|9|8:13] #Anglais[10,5|9:15] #PC[10|13:11]  #SVT[12|11|16|8:12]  #HG[10:10]'
note=""
devoir = []
numero = numeroValide(input("Donner votre numero\n"))
nom = prenomValide(input("Donner Votre nom\n"))
prenom = nomValide(input('Donner Votre prenom\n'))
date = changerFormatDate(input("Donner Votre date de naissance\n"))
classe = definirFormatClasse(input("Donner votre nom de classe\n"))
nbr_matieres = int(input(" Donner le nombre de  matieres\n"))
while nbr_matieres > 0:
    matiere = input("Donner le nom de la matiere\n")
    note += matiere
    nbr_matieres -= 1
    print("Donner le nombre de devoir de ",matiere)
    nbre_devoir = int(input())
    for i in range(1,nbre_devoir+1):
        print("Donner le devoir N°",i)
        dev = float(input())
        devoir.append(dev)
    examen =float(input("Donner la note d'examen\n"))
    devoir.append(examen)      
    note += str(devoir)+ "#" 
    devoir =[]
not = noteValide(note)    




    
    