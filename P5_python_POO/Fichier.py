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
        for line in liste_eleves:
            eleve = Eleve(line["numero"],line["nom"],line["prenom"],line["date de naissance"],line["classe"],line["note"])
            numero = eleve.numeroValide(eleve.num)
            nom = eleve.nomValide(eleve.nm)
            prenom = eleve.prenomValide(eleve.prenm)
            forma_date = eleve.changerFormatDate(eleve.date_n)
            print("formadate",forma_date)
            if forma_date == False:
                continue
            date_valide = eleve.dateValide(forma_date)
            print("datevalide",date_valide)
            forma_classe = eleve.definirFormatClasse(eleve.cl)
            if forma_classe == False:
                continue
            valide_classe = eleve.classeValide(forma_classe)
            note_valide = eleve.noteValide(eleve.notee)
            if numero == True and nom == True and prenom == True and forma_date != False and date_valide == True and forma_classe != False and valide_classe == True and note_valide != False:
                liste_valide.append(line)
                #print("test",line)
            else:
                liste_invalide.append(line)

        return liste_valide,liste_invalide        




fichier = Fichier()
listeEleves = fichier.lesEleves("data.csv")  
liste_valide,liste_invalide=fichier.valide_invalide(listeEleves)
# for line in liste_invalide:
#     print(line)
# for line in liste_valide:
#     print(line)
