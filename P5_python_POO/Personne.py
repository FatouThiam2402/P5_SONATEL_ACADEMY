from datetime import *
import csv
import re

class Eleve:

    def __init__(self):
        pass
    
    def __init__(self,numero,nom,prenom,date_naiss,classe,note):
        self.num = numero
        self.nm = nom
        self.prenm = prenom
        self.date_n = date_naiss
        self.cl = classe
        self.notee  = note        

    def numeroValide(self,chaine):
        if len(chaine) == 7:
            if chaine.isalnum() == True:
                if chaine.isupper() == True:
                    if any(c.isdigit()for c in chaine) == True:
                        
                        return True    
    
        
    def prenomValide(self,prenom):
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


    def nomValide(self,nom):
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


    def enleverspace(chaine):
        ch=""
        if chaine[0] != " ":
            ch+=chaine[0]
        for i in range(1,len(chaine)):
            if (chaine[i-1] == " " and chaine[i]== " "):
                continue
            else:
                ch+=chaine[i]
        return ch
            

    def changerFormatDate(self,date):

        if date == "" or date == " ":
            return False
        Eleve.enleverspace(date)
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


    def dateValide(sef,date):
        date = date.split("-")
        jour = int(date[0])
        mois = int(date[1])
        annee = int(date[2]) 
       
        try:
            date = datetime(annee,mois,jour).strftime("%d-%m-%y")
            
        except:
            return False
        return True             


    def definirFormatClasse(self,classe):
        cl =""
        if classe == "" or classe == " ":
            return False
        else:
            cl = classe[0]+" "+"iem"+" "+classe[len(classe) - 1]
        return cl
    

    def classeValide(self,cl):
        classValide=""
        if cl[0] in ["6","5","4","3"] and cl[len(cl) - 1] in ["A","B"]:
            classValide += cl
            return True
        else:
            return False

    def noteValide(self,note):
        note = note.replace("Science_Physique","PC")
        note = note.replace("pc","PC")
        note = note.replace("ANGLAIS","Anglais")
        note = note.replace("FRANCAIS","Francais")
        note = note.replace("Français","Francais")
        note = note.replace("MATH","Math")

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
            elemtSub = elemtSub.replace(';',':')
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







        

