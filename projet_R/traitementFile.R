
url <- "/Volumes/maman/P5-son@tel-académie/P5_SONATEL_ACADEMY/projet_R"
import::from(pins::pin(url), "LesFonctions", .character_only=TRUE)

################################################################################
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

################################################################################
nom_valide <- function(nom){
  if(grepl("^[A-Za-z]",nom) & sum(grepl("[[:alpha:]]",strsplit(nom,"")[[1]])) >= 2)
  {return (TRUE)} 
  else {return (FALSE)}
}
################################################################################
prenom_valide <- function(prenom){
  if(grepl("^[A-Za-z]",prenom) & sum(grepl("[[:alpha:]]",strsplit(prenom,"")[[1]])) >= 3)
  {return (TRUE)} 
  else {return (FALSE)}
}

################################################################################
valide_date <- function(date){
  tmp <- ""
  date <- trimws(date)
  date = str_replace_all(date,c("fev"="02","janvier"="02","mars"="03","avril"="04","mai"="05","juin"="06","juillet"="07","août"="08","septembre"="09","octobre"="10","novembre"="11","décembre"="12","dècembre"="12","decembre"="12"))
  date = str_replace_all(date,c("-"="/",":"="/",","="/",";"="/"," "="/","\\|"="/","\\." = "/"))
  
  if(!(is.na(as.Date(date,format = "%d/%m/%Y")))){return (TRUE)} else{return (FALSE)}
  
}

################################################################################
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

################################################################################
valide_note <- function(note){
  note <- gsub(" ","",note)
  if(substring(note,1,1) == '#'){ 
    note <- substring(note,2,nchar(note))
  }
  note
  note <- strsplit(note,"#")
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

################################################################################






df_csv = read.csv("data100code.csv",sep=",")
df_csv1 <- df_csv[!apply(df_csv == "", 1, all), ] # cette instruction permet de prendre toutes les lignes sauf les lignes vides

#######################################################
numero <- sapply(df_csv1$Numero, numero_valide)       #
nom <- sapply(df_csv1$Nom, nom_valide)                #
prenom <- sapply(df_csv1$Prénom, prenom_valide)       #
date <- sapply(df_csv1$Date.de.naissance, valide_date)#
classe <- sapply(df_csv1$Classe, valide_classe)       #
note <- sapply(df_csv1$Note, valide_note)   
note      #
#########################################################

date <- df_csv1[(sapply(df_csv1$Date.de.naissance, valide_date)),]
nrow(date)
data_valide <- df_csv1[sapply(df_csv1$Numero, numero_valide) & sapply(df_csv1$Nom, nom_valide) & sapply(df_csv1$Prénom, prenom_valide) &  sapply(df_csv1$Date.de.naissance, valide_date) & sapply(df_csv1$Classe, valide_classe),]
data_invalide <- df_csv1[!sapply(df_csv1$Numero, numero_valide) | !sapply(df_csv1$Nom, nom_valide) | !sapply(df_csv1$Prénom, prenom_valide) | !sapply(df_csv1$Date.de.naissance, valide_date) | !sapply(df_csv1$Classe, valide_classe),]
data_invalide

write.csv(data_valide,"data_valide.csv")
write.csv(data_invalide,"data_invalide.csv")

  

