1
menu = 1

while menu in [1,2,3,4,5]:
    print(50*"")
    print(10*" ","Voici le Menu: \n 1• Afficher les informations\n 2•Afficher une information par son Numero\n 3•afficher les cinq premiers par leur moyenne \n 4• Ajouter une Information \n 5• Modifier une information Invalide\n 6•Pour Quitter")
    print(50*"")
    menu = int(input())
    if menu == 1:
        sous_menu = int(input("choisir entre données valide ou invalide\n 1• Afficher les informations Valides \n 2• Afficher les informations Invalides\n"))
        if sous_menu == 1:
            print("methode affichage valide")
        elif sous_menu == 2:
            print("methode affichage invalide")    
    elif menu == 2:
        print("mehtode affichage info par son numero")
    elif menu == 3:
        print("methode affichage 5 premiers par leur moyenne")   
    elif menu == 4:
        print("methode ajouter une information")
    elif menu == 5:
        print("methode affichage modifier une information invalide")
    else:
        exit            

    