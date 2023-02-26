
# import re

# note = '#Math[10.5|15:15] #Francais[17|9|8:13] #Anglais[10,5|9:15] #PC[10|13:11]  #SVT[12|11|16|8:12]  #HG[10:10]'

# def noteValide(note):
#     listemoyAnnuel =[]
#     moyAnnuel = 1
#     somMoyenMatieres =0
#     matieresNotes = note.split("#")
#     if matieresNotes[0] == '':
#         del matieresNotes[0]
#     else:
#         print()    
#     listeMat = []
#     for elemt in matieresNotes:
#         elemtSub = re.sub('[|]',':',elemt)
#         elemtSub = elemtSub.replace(']',':')
#         elemtSub = elemtSub.replace('[',':')
#         elemtSub = elemtSub.replace(',','.')
#         elemtSub = elemtSub.replace(" ","")
#         elemtSub = elemtSub.split(':')
#         del elemtSub[len(elemtSub) -1]
#         if elemtSub == "" or elemtSub == " " or len(elemtSub) <= 1:
#             return False
#         for i in range(1,len(elemtSub)): 
#             for c in elemtSub[i]:
#                 if c not in ["0","1","2","3","4","5","6","7","8","9","."]:
#                     return False 
#         #if elemtSub[i]                  
#         elemtSub = "-".join(elemtSub)
#         elemtSub = elemtSub.strip()
#         elemtSub = elemtSub.split("-")
#         for i in range(len(elemtSub)):
#             if elemtSub[i] == "" or elemtSub[i] == " ":
#                elemtSub[i] = elemtSub[i].replace("","0.0")            
#         s = 0
#         nbr = 0
#         moy = 1
#         examen = 0
#         for i in range(1,len(elemtSub)- 1):
#             # if(float(elemtSub[i]) < 0 and float(elemtSub[i]) > 20):
#             #     return False
#             # else:
#             s += float(elemtSub[i])
#             nbr += 1      
#         examen += float(elemtSub[len(elemtSub) - 1])  
#         moy += round((((s / nbr) + 2*examen) / 3),2)
#         elemtSub.append(moy)
#         listeMat.append(elemtSub)
#         elemtSub=[]
#         somMoyenMatieres+=moy     
#     moyAnnuel =round(somMoyenMatieres/len(matieresNotes),2)
#     listemoyAnnuel.append(moyAnnuel)    
    
#     return listeMat,listemoyAnnuel

# liste=[1,-3,10,4,100,-10]
# listeMax = []
# for i in range(len(liste)):
#     max = liste[i]
#     for j in range(i+1,len(liste)):
#         if liste[j] > max:
#             tmp = max
#             max = liste[j]
#             liste[j]=tmp
#     listeMax.append(max)       

# print(listeMax)

# listeMax=[['Math', '10.5', '15', '15', 15.25], ['Francais', '17', '9', '8', '13', 13.44], 
# ['Anglais', '10.5', '9', '15', 14.25], ['PC', '10', '13', '11', 12.17],
#  ['SVT', '12', '11', '16', '8', '12', 12.92], ['HG', '10', '10', 11.0]]

# def calculMoyenGeneral(listeMat):
#     moyAnnuel = 1
#     somMoyenMatieres =0
#     for line in listeMat:
#         somMoyenMatieres += line[len(line)- 1]    
#     moyAnnuel = round(somMoyenMatieres/len(listeMat),2)
#     return moyAnnuel

# print("moyenne",calculMoyenGeneral(listeMax))
#************************************************
liste_global =[]
liste_dict =[]

liste = [[12,"Fatou","THIAM"], [4,"absa","diop"],[5,"coumba","top"]]
for line in liste:
    dict_tmp = {}
    dict_tmp["Numero"] = line[0]
    dict_tmp["Prenom"] = line[1]
    dict_tmp["Nom"] = line[2]


    liste_dict.append(dict_tmp)

print(liste_dict)

for line in liste_dict:
    #print(line)
    pass
#************************************************************


