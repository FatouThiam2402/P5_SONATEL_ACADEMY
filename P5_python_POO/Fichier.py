from Personne import * 
import json
from lxml import etree


class Fichier:
     
    def __init__(self):
          pass


    def lesEleves(self,nomfichier):

        liste_eleves = []
        dict_eleve = {}

        file_csv = csv.reader(open(nomfichier), delimiter=',')

        for line in file_csv:
            eleve = Eleve(line[1],line[2],line[3],line[4],line[5],line[6])
            dict_eleve={"numero":eleve.num,"nom":eleve.nm,"prenom":eleve.prenm,"date de naissance":eleve.date_n,"classe":eleve.cl,"note":eleve.notee}
            liste_eleves.append(dict_eleve)            
        return liste_eleves
    

    def valide_invalide(self,liste_eleves):
        liste_valide = list()
        liste_invalide = list()
        liste_note_valide =list()
        liste_note_invalide =list()
        dict_tmp ={}
        dict_note_tmp={}
        for line in liste_eleves:
            eleve = Eleve(line["numero"],line["nom"],line["prenom"],line["date de naissance"],line["classe"],line["note"])
            numero = eleve.numeroValide(eleve.num)
            nom = eleve.nomValide(eleve.nm)
            prenom = eleve.prenomValide(eleve.prenm)
            note_valide = eleve.noteValide(eleve.notee)
            forma_date = eleve.changerFormatDate(eleve.date_n)
            if forma_date == False:
                dict_tmp={"numero":line["numero"],"nom":line["nom"],"prenom":line["prenom"],"date de naissance":line["date de naissance"],"classe":line["classe"]}
                dict_note_tmp={"numero":line["numero"],"note":line["note"]}
                liste_invalide.append(dict_tmp)
                liste_note_invalide.append(dict_note_tmp)
                continue
            date_valide = eleve.dateValide(forma_date)
            forma_classe = eleve.definirFormatClasse(eleve.cl)
            if forma_classe == False:
                liste_invalide.append(line)
                continue
            valide_classe = eleve.classeValide(forma_classe)
            dict_tmp={"numero":line["numero"],"nom":line["nom"],"prenom":line["prenom"],"date de naissance":forma_date,"classe":forma_classe}
            dict_note_tmp={"numero":line["numero"],"note":note_valide}
            if numero == True and nom == True and prenom == True and forma_date != False and date_valide == True and forma_classe != False and valide_classe == True and note_valide != False:
                liste_valide.append(dict_tmp)
                liste_note_valide.append(dict_note_tmp)
            else:
                dict_tmp={"numero":line["numero"],"nom":line["nom"],"prenom":line["prenom"],"date de naissance":line["date de naissance"],"classe":line["classe"]}
                dict_note_tmp={"numero":line["numero"],"note":line["note"]}
                liste_invalide.append(dict_tmp)
                liste_note_invalide.append(dict_note_tmp)

        return liste_valide,liste_note_valide,liste_invalide,liste_note_invalide        

    def afficherInfos(self,list_valides):
        print(53*"-")
        print ("{:<8} {:<8} {:<10} {:<15} {:<10}".format('Numéro','Nom','Prenom','Date de naissance','Classe'))
        print(53*"-")
        for line in list_valides:
            print("{:<8} {:<8} {:<10} {:<15} {:<10}".format(line["numero"], line["nom"],line["prenom"], line["date de naissance"], line["classe"]))
        
    def afficherNoteValide(self,list_note_valides):
        print(60*"-")
        print('   Numéro\tNotes devoirs Examen Moyenne')
        for line in list_note_valides:
            print(60*"-")
            print(line["numero"])
            for matiere in line["note"]:
                print("\t\t",matiere)
        print(60*"-")  

    def afficherNoteInValide(self,list_note_invalides):
        print(100*"-")
        print('   Numéro\tNotes devoirs Examen Moyenne')
        for line in list_note_invalides:
            if line["numero"] ==" " and  line["note"] == "":
                continue
            print(60*"-")
            print("Numero",line["numero"])
            print("Note:",line["note"])
        print(60*"-")  


    def afficherUneInfo(self,numero,liste_valide,liste_inval,list_note_valides,list_note_invalides):
        print(53*"-")
        print ("{:<8} {:<8} {:<10} {:<15} {:<10}".format('Numéro','Nom','Prenom','Date de naissance','Classe'))
        print(53*"-")
        for line in liste_valide:
            if line["numero"] == numero:
                print("{:<8} {:<8} {:<10} {:<15} {:<10}".format(line["numero"], line["nom"],line["prenom"], line["date de naissance"], line["classe"]))

        for line in liste_inval:
            if line["numero"] == numero:
                print("{:<8} {:<8} {:<10} {:<15} {:<10}".format(line["numero"], line["nom"],line["prenom"], line["date de naissance"], line["classe"]))
        print(53*"-")
        for line in list_note_valides:
            if line["numero"] == numero:
                print(line)
        for line in list_note_invalides:
            if line["numero"] == numero:
                print(60*"-")
                print('   Numéro\tNotes devoirs Examen Moyenne')
                print(60*"-")
                print(line["Numero"])
                print(line["note"])
                print(60*"-")    
      
#def afficher5premiersDeLaClasse(liste):

    def calculMoyenGeneral(self,listeMat):
        moyAnnuel = 1
        somMoyenMatieres =0
        for line in listeMat:
            somMoyenMatieres += line[len(line)- 1]    
        moyAnnuel = round(somMoyenMatieres/len(listeMat),2)
        return moyAnnuel

    def afficherLes5premiers(self,list_note_valides):
        fichier = Fichier()
        list_moy_Generale = []
        for row in list_note_valides:
            MoyGeneralEtud = fichier.calculMoyenGeneral(row["note"])
            dict_moy_Generale = {"numero":row["numero"],"moyen_general":MoyGeneralEtud}
            list_moy_Generale.append(dict_moy_Generale)
            dict_moy_Generale={}
        dict_moy_croissant = sorted(list_moy_Generale , key=lambda d:d['moyen_general'],reverse = True)
        j = 0
        for i in range(1,len(dict_moy_croissant)):
            while j<6:
                print(dict_moy_croissant[i])
                j+=1


#def afficher5premiers():

    def ajouterInfo(self):
            note=""
            devoir = []
            numero = input("Donner votre numero\n")
            nom = input("Donner Votre nom\n")
            prenom = input('Donner Votre prenom\n')
            date = input("Donner Votre date de naissance\n")
            classe = input("Donner votre nom de classe\n")

            nbr_matieres = int(input(" Donner le nombre de  matieres\n"))
            while nbr_matieres > 0:
                matiere = input("Donner le nom de la matiere\n")
                note += "#"+ matiere
                nbr_matieres -= 1
                print("Donner le nombre de devoir de ",matiere)
                nbre_devoir = int(input())
                for i in range(1,nbre_devoir+1):
                    print("Donner le devoir N°",i)
                    dev = float(input())
                    devoir.append(dev)
                examen =float(input("Donner la note d'examen\n"))
                devoir.append(examen)
                note += str(devoir)
                devoir =[]
            note1 = note.replace(',',';')

            eleve = Eleve(numero,nom,prenom,date,classe,note1)
            num_val = eleve.numeroValide(numero)
            if num_val == False:
                print("Le numero est invalide")
            nom_val = eleve.nomValide(nom)
            if nom_val == False:
                print("Le nom saisi n'est pas correcte car < 2\n")
            prenom_val = eleve.prenomValide(prenom)
            if prenom_val == False:
                print("Le prenom saisi n'est pas correcte car < 3\n")
            forma_date_val = eleve.changerFormatDate(date)
            if forma_date_val == False:
                print("la date est invalide\n ")
            else:    
                date_val = eleve.dateValide(forma_date_val)
                if date_val == False:
                    print("La date est incorrecte/n")
                else:
                    pass    
            forma_classe_val = eleve.definirFormatClasse(classe)
            if forma_classe_val == False:
                print("La classe n'existe pas")
            classe_val = eleve.classeValide(forma_classe_val)
            if classe_val == False:
                print(" La classe saisi est incorreste\n")
            
            noteF = eleve.noteValide(note1)
            if noteF == False:
                print("Les notes saisies sont incorrectes\n")
            else:
                pass   
            
            if num_val == True and nom_val == True and prenom_val == True and date_val == True and classe_val == True and noteF != False:
                print("Toutes les informations saisies sont correctes")
            else:
                print("Il existe des informations incorrectes\n")   


class principal:

    fichier = Fichier()
    listeEleves = fichier.lesEleves("data.csv")  
    liste_valide,liste_note_valide,liste_invalide,liste_note_invalide=fichier.valide_invalide(listeEleves)
  
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
                fichier.afficherInfos(liste_valide)
                print("nbre",len(liste_valide))
                fichier.afficherNoteValide(liste_note_valide)
            elif sous_menu == 2:
                print("methode affichage invalide")
                fichier.afficherInfos(liste_invalide) 
                fichier.afficherNoteInValide(liste_note_invalide)
        elif menu == 2:
            numero =input("Entrer votre numero svp")
            fichier.afficherUneInfo(numero,liste_valide,liste_invalide,liste_note_valide,liste_note_invalide)
        elif menu == 3:
                fichier.afficherLes5premiers(liste_note_valide)  
        elif menu == 4:
                fichier.ajouterInfo()
                
        elif menu == 5:
            print("En cours de traitement")
        else:
            exit    

