import csv
import re
import datetime

def numeroValide(chaine):
    if len(chaine) == 7:
        if chaine.isalnum() == True:
            if chaine.isupper() == True:
                if any(c.isdigit()for c in chaine) == True:
                    
                    return True
                else:
                    return False   

                

def prenomValide(prenom):
    cnt = 1
    if (prenom == ""):
        return False
    elif prenom[0] >= 'a' and prenom[0] <= 'z' or prenom[0] >= 'A' and prenom[0] <= 'Z':
        for i in range(1,len(prenom)):
            if prenom[i] >= 'a' and prenom[i] <= 'z' or prenom[i] >= 'A' and prenom[i] <= 'Z':
                cnt += 1
        if cnt >= 3:
            return True
        else:
            return False    
    else:
        return False        
#print(prenomValide("1de"))       

def nomValide(nom):
    nbre = 1
    if (nom == ""):
        return False
    elif nom[0] >= 'a' and nom[0] <= 'z' or nom[0] >= 'A' and nom[0] <= 'Z':
        for i in range(1,len(nom)):
            if nom[i] >= 'a' and nom[i] <= 'z' or nom[i] >= 'A' and nom[i] <= 'Z':
                nbre += 1
        if nbre >= 2:
            return True 
        else:
            return False
        
    else:
        return False        
#print(nomValide("1ez"))        
#######   REvoir la date psk ça marche plus  ###########
def changerFormatDate(date):
    dateF =""
    listeMois =["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","decembre"]
    listeSep =[' ',',','-',';','_','/','.',':']
    if date == "" or date == " ":
        return False
    else:    
        for c in date:
            if c in listeSep:
                sep=c
                dateF = date.replace(sep,"-")     
        dateL = dateF.split("-")
        if len(dateL) == 3:
            for i  in range(len(listeMois) -  3):
                if listeMois[i] == dateL[1]:
                    dateL[1] = "0"+str(i + 1)
            for j in  range(9,len(listeMois)):
                if listeMois[j] == dateL[1]:
                    dateL[1] =str(j + 1)
            dateL = "-".join(dateL)
            for c in dateL:
                if c not in ["0","1","2","3","4","5","6","7","8","9","-"]:
                    return False                       
                return dateL
        else:
         return False


#print("test1",changerFormatDate("23/octobre/2o00"))


     
# verification de la validité de la date
def dateValide(date):
    date = date.split("-")
    print("================================÷\n\n\n\n\n")
    print(date)
    jour = int(date[0])
    mois = int(date[1])
    annee = int(date[2])
    try:
        date = datetime.datetime(annee,mois,jour).strftime("%d-%m-%y")
    except:
        return False
    return True   
#print(dateValide(changerFormatDate("22/mars/2003")))
#print("verification",dateValide(changerFormatDate("29/mars/09")))

def definirFormatClasse(classe):
    cl =""
    if classe == "" or classe == " ":
        return False
    else:
        cl = classe[0]+" "+"iem"+" "+classe[len(classe) - 1]
    return cl
#print(definirFormatClasse(" "))

def classeValide(cl):
    classValide=""
    if cl[0] in ["6","5","4","3"] and cl[len(cl) - 1] in ["A","B"]:
        classValide += cl
        return True
    else:
        return False    
          

#print(classeValide(definirFormatClasse(" ")))

import re

note = '#Math[10.5|15:15] #Francais[17|9|8:13] #Anglais[10,5|9:15] #PC[10|13:11]  #SVT[12|11|16|8:12]  #HG[10:10]'

def noteValide(note):
    matieresNotes = note.split("#")
    if matieresNotes[0] == '':
        del matieresNotes[0]
    else:
        pass    
    listeMat = []
    for elemt in matieresNotes:
        elemtSub = re.sub('[|]',':',elemt)
        elemtSub = elemtSub.replace(']',':')
        elemtSub = elemtSub.replace('[',':')
        elemtSub = elemtSub.replace(',','.')
        elemtSub = elemtSub.replace(" ","")
        elemtSub = elemtSub.split(':')
        del elemtSub[len(elemtSub) -1]
        if elemtSub == "" or elemtSub == " " or len(elemtSub) <= 1:
            return False
        for i in range(1,len(elemtSub)): 
            for c in elemtSub[i]:
                if c not in ["0","1","2","3","4","5","6","7","8","9","."]:
                    return False   
        #if elemtSub[i]                  
        elemtSub = "-".join(elemtSub)
        elemtSub = elemtSub.strip()
        elemtSub = elemtSub.split("-")
        for i in range(len(elemtSub)):
            if elemtSub[i] == "" or elemtSub[i] == " ":
               elemtSub[i] = elemtSub[i].replace("","0.0")            
        s = 0
        nbr = 0
        moy = 1
        examen = 0
        for i in range(1,len(elemtSub)- 1):
            # if(float(elemtSub[i]) < 0 and float(elemtSub[i]) > 20):
            #     return False
            # else:
            s += float(elemtSub[i])
            nbr += 1      
        examen += float(elemtSub[len(elemtSub) - 1])  
        moy += round((((s / nbr) + 2*examen) / 3),2)
        elemtSub.append(moy)
        listeMat.append(elemtSub)
        elemtSub=[]    
    return listeMat

#listemat,listemoyAnnuel = noteValide(note)
def calculMoyenGeneral(listeMat):
    moyAnnuel = 1
    somMoyenMatieres =0
    for line in listeMat:
        somMoyenMatieres += line[len(line)- 1]    
    moyAnnuel = round(somMoyenMatieres/len(listeMat),2)
    return moyAnnuel

#print("moyennn",calculMoyenGeneral(noteValide(note)))

def afficherInfoValides(list_valides):
    print(53*"-")
    print ("{:<8} {:<8} {:<10} {:<15} {:<10}".format('Numéro','Nom','Prenom','Date de naissance','Classe'))
    print(53*"-")
    for line in list_valides:
        print("{:<8} {:<8} {:<10} {:<15} {:<10}".format(line["Numero"], line["Nom"],line["Prenom"], line["Date de naissance"], line["Classe"]))
    
def afficherNoteValide(list_note_valides):
    print(60*"-")
    print('   Numéro\tNotes devoirs Examen Moyenne')
    for line in list_note_valides:
        print(60*"-")
        print(line["Numero"])
        for matiere in line["Note"]:
            print("\t\t",matiere)
            # for note in matiere:
            #     print("\t\t",str(note)+(15-len(str(note)))*" ",end=" ")
            # print()
    print(60*"-")  
        

def afficherUneInfo(numero,liste_valide,liste_inval,list_note_valides,list_note_invalides):
    print(53*"-")
    print ("{:<8} {:<8} {:<10} {:<15} {:<10}".format('Numéro','Nom','Prenom','Date de naissance','Classe'))
    print(53*"-")
    for line in liste_valide:
        if line["Numero"] == numero:
            print("{:<8} {:<8} {:<10} {:<15} {:<10}".format(line["Numero"], line["Nom"],line["Prenom"], line["Date de naissance"], line["Classe"]))

    for line in liste_inval:
        if line["Numero"] == numero:
            print("{:<8} {:<8} {:<10} {:<15} {:<10}".format(line["Numero"], line["Nom"],line["Prenom"], line["Date de naissance"], line["Classe"]))
    print(53*"-")
    for line in list_note_valides:
        if line["Numero"] == numero:
            print(line)
    for line in list_note_invalides:
        if line["Numero"] == numero:
            print(60*"-")
            print('   Numéro\tNotes devoirs Examen Moyenne')
            print(60*"-")
            print(line["Numero"])
            for matiere in line["Note"]:
                print("\t\t",matiere)
            print(60*"-")    
      


      





#def afficher5premiersDeLaClasse(liste):



def afficherUneNote(numero,liste_note_val,liste_note_inval):
    print(53*"-")
    print ("{:<8} {:<15} ".format('Numéro','Note'))
    print(53*"-")
    for line in liste_note_val:
        if line["Numero"] == numero:
            print("{:<8}  {:<15}".format(line["Numero"], line["Note"]))
    for line in liste_note_inval:
        if line["Numero"] == numero:
            print("{:<8}  {:<15}".format(line["Numero"], line["Note"]))
    print(53*"-")                

    


#def afficher5premiers():
def ajouterInfo():
    note=""
    devoir = []
    numero = numeroValide(input("Donner votre numero\n"))
    if numero == False:
        print("Le numero est invalide")
    nom = prenomValide(input("Donner Votre nom\n"))
    if nom == False:
        print("Le nom saisi n'est pas correcte car < 2\n")
    prenom = nomValide(input('Donner Votre prenom\n'))
    if prenom == False:
        print("Le prenom saisi n'est pas correcte car < 3\n")
    forma_date = changerFormatDate(input("Donner Votre date de naissance\n"))
    if forma_date == False:
        print("la date est invalide\n ")
    else:    
        date = dateValide(forma_date)
        if date == False:
            print("La date est incorrecte/n")
        else:
            pass    
    forma_classe = definirFormatClasse(input("Donner votre nom de classe\n"))
    if forma_classe == False:
        print("La classe n'existe pas")
    classe = classeValide(forma_classe)
    if classe == False:
        print(" La classe saisi est incorreste\n")
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
    noteF = noteValide(note1)
    if noteF == False:
        print("Les notes saisies sont incorrectes\n")
    else:
       pass   
       
    if numero == True and nom == True and prenom == True and forma_date != False and date == True and forma_classe != False and classe == True and noteF != False:
        print("Toutes les informations saisies sont correctes")
    else:
        print("Il existe des informations incorrectes\n")    









    

