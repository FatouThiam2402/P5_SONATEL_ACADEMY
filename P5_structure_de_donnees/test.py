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
         
print(changerFormatDate("24/03/99"))         