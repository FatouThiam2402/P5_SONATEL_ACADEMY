import datetime
  # date_bon =[]
    # if len(date[2]) == 4:
    #     if date[1] in ["01","03","05","07","08","10","12"] and int(date[0]) <= 31:
    #         date_bon += date
    #         return "-".join(date_bon)
    #     elif date[1] in ["04","06","09","11"] and int(date[0]) <= 30:
    #         date_bon += date
    #         return date_bon
    #     elif (date[1] == "02") and (int(date[0]) <= 28):
    #         date_bon += date
    #         return date_bon
    #     elif (date[1] == "02") and (int(date[0]) == 29) and (((int(date[2])) % 4 == 0 and (int(date[2])) % 100 == 0) or  ((int(date[2])) % 400 == 0)):
    #         date_bon += date
    
            # elif (int(date[2]) % 4 != 0 or int(date[2]) % 100 != 0) and  (int(date[2]) % 400 != 0) or (int(date[1]) <= 28):
            #     date_bon += date
            #     return date_bon



def transformerDate(date):
    # print(".....................")
    # print(changerFormatDate("23/02/2022"))
    listeMois =["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"]
    d = date.split("-")
    # print(d)
    for i  in range(len(listeMois)- 3):
        if  listeMois[i] == d[1]:
            d[1] = "0"+str(i + 1)
    for i in  range(9,len(listeMois)):
        if  listeMois[i] == d[1]:
            d[1] =str(i + 1)    
            print(d)
        return d       
# print("__________________")        
#print(transformerDate(changerFormatDate("23/02/2022")))  
#  "-".join(d)             




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
            return dateL.split("-")
        else:
            return False    
print("111111",changerFormatDate("23;mars;2000"))


     
# verification de la validité de la date
def dateValide(date):
    #date = "-".join(date)
    
    #date = date.split("-")
    jour = int(date[0])
    mois = int(date[1])
    annee = int(date[2])
    try:
        date = datetime.datetime(annee,mois,jour).strftime("%d-%m-%y")
    except:
        return False
    return date   
d = changerFormatDate(" 12/février/2004")    
print("verification",dateValide(d))


