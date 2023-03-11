library(stringr)
library("dplyr")


numero_valide <- function(numero){
  caract = "^[A-Z]{7}$"
  chiffre = "^[0-9]{7}$"
  caract_chiffre = "^[A-Z0-9]{7}$"
  if(grepl(caract,numero))
  { return (FALSE)}
  else{
    if(grepl(chiffre,numero))
    {return (FALSE)}
    else{
      if(grepl(caract_chiffre,numero))
        {return (TRUE)}
      else{return (FALSE)}
    }
  }
}

#numero_valide("1A11111")
nom_valide <- function(nom){
   if(grepl("^[A-Za-z]",nom) & sum(grepl("[[:alpha:]]",strsplit(nom,"")[[1]])) >= 2)
      {return (TRUE)} 
   else {return (FALSE)}
}

#nom_valide("zz2")
prenom_valide <- function(prenom){
  if(grepl("^[A-Za-z]",prenom) & sum(grepl("[[:alpha:]]",strsplit(prenom,"")[[1]])) >= 3)
    {return (TRUE)} 
  else {return (FALSE)}
}


valide_date <- function(date){
  tmp <- ""
  date <- trimws(date)
  date = str_replace_all(date,c("fev"="02","janvier"="02","mars"="03","avril"="04","mai"="05","juin"="06","juillet"="07","août"="08","septembre"="09","octobre"="10","novembre"="11","décembre"="12","dècembre"="12","decembre"="12"))
  date = str_replace_all(date,c("-"="/",":"="/",","="/",";"="/"," "="/","\\|"="/","\\." = "/"))
 
  if(!(is.na(as.Date(date,format = "%d/%m/%Y")))){return (date)} else{return (FALSE)}
  
}

#valide_date("25 marms|2017")
# paste0 : permet concaténer
valide_classe <- function(cl){
  trimws(cl)
  nb <- nchar(cl)
  classe_split <- strsplit(cl,"")
  classe <- paste0(classe_split[[1]][1],"ieme",classe_split[[1]][nb])
  nbr <- nchar(classe)
  substring(classe,1,1)
  nbr
  if(substring(classe,1,1) %in% c(3:6 ) && substring(classe,nbr,nbr) %in% c("A","B"))
    {return (TRUE)} 
  else
  {return(FALSE)}
}
#valide_classe("1hgghdggdemA")

#if(grepl("^3",classe) & grepl("A$",classe)){return (TRUE)} else{return (FALSE)}
# substring(classe,1,1)
# substring(classe,nbr,nbr)
# 
# niveau <- c("6","5","4","3")
# type <- c("A","B")
# 
# if(grepl(substring(classe,1,1),classe )){ return(TRUE)} else{return(FALSE)}


valide_note <- function(note){
  
  

  note <- gsub(" ","",note)
  note
  note <- strsplit(note,"#")
  note
  if (note[[1]][1] == ""){
    note <- note[[1]][-1]
  }
  for(matiere in note)
  {
    matiere <- str_replace_all(matiere,c("\\[" = ':',"\\|" = ":","]" = ":","," = "."))
    matiere <- strsplit(matiere,":")
    if(length(matiere[[1]]) >= 3)
    {
      n_note <- matiere[[1]][-1]
      for(n in n_note){
        if(as.numeric(n) >= 0 & as.numeric(n) <= 20){ return(TRUE)}  else {return(FALSE)}
      }
    }
  }
}










####################  partie TEST hors des FONCTIONS#######################

note <- '#Math[10.5|15:15] #Francais[17|19|8:13] #Anglais[10,5|9:15] #PC[10|13:11]  #SVT[12|11|16|8:12]  #HG[10:10]'

note <- gsub(" ","",note)
note

if(substring(note,1,1) == '#'){ 
  note <- substring(note,2,nchar(note))
  print("eliminer #")
  print(note)
  
}
note <- strsplit(note,"#")

for(matiere in note)
  {
    matiere <- str_replace_all(matiere,c("\\[" = ':',"\\|" = ":","]" = ":","," = "."))
    matiere <- strsplit(matiere,":")
    if(length(matiere[[1]]) >= 3)
      {
        n_note <- matiere[[1]][-1]
        for(n in n_note)
        {
          if(as.numeric(n) >= 0 & as.numeric(n) <= 20){ print("TRUE")}  else {print("FALSE")}
        }
  
     }

  }
  

  


      
  
  







