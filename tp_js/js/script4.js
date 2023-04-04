
const resultat_pw = document.getElementById("resultat_passwordGenerer");
const taille_pw = document.getElementById("taille_passwd");
const pw_lettres_majuscule = document.getElementById("lettres_majuscule");
const pw_lettres_minuscule = document.getElementById("lettres_minuscule");
const pw_nombres = document.getElementById("nombres");
const pw_caracteres_speciaux = document.getElementById("caracteres_speciaux");
const btn_generer_passwd = document.getElementById("btn_generer_passwd");



// 97 - 122 codes  a-z 
//  65- 90 codes A-Z
// 48-57 codes 0-9

function generer_pw_lettres_majuscule(){
	return String.fromCharCode((Math.floor(Math.random()*26)+65));
}


function generer_pw_lettres_minuscule(){
	return String.fromCharCode((Math.floor(Math.random()*26)+97));
}


function generer_pw__chiffres(){
	return String.fromCharCode((Math.floor(Math.random()*10)+48));
}


function generer_pw_caracteres_speciaux(){

	const speciaux ="!@#$£%&*(){}[]=<>/,.^"; 

	return speciaux[Math.floor(Math.random()*speciaux.length)];
	
}

const les_Fonctions = {
	majuscule:generer_pw_lettres_majuscule,
	minuscule:generer_pw_lettres_minuscule,
	chiffre:generer_pw__chiffres,
	speciaux:generer_pw_caracteres_speciaux
}


function generer_passWord(majuscule,minuscule,chiffre,speciaux,taille_password){
	let passWord="";

	const typecontent = majuscule + minuscule + chiffre + speciaux; // typecontent contient le nombre de champs checked.  // il filtre des elements en recupérant juste les True.

	
	const types_arr = [{majuscule},{minuscule},{chiffre},{speciaux}].filter(i => Object.values(i)[0]);

	if(typecontent == 0){
		return ""
	}
	for(let i = 0; i < taille_password; i+= typecontent){

		types_arr.forEach(element =>{
			const cle = Object.keys(element)[0];
			 passWord += les_Fonctions[cle]();
		});
		
	}
	return passWord
}


/*console.log(types_arr); voici le resultat ->
0: {click_majuscule: false}
1: {click_minuscule: false}
2: {click_number: false}
3: {click_speciaux: false}
length: 4
*/

// Object.keys() donne les clés de l'objet
// Object.keys(element)[0] affiche la premiere clé



btn_generer_passwd.addEventListener("click",function(){

	const taille_password = taille_pw.value;
	const majuscule = pw_lettres_majuscule.checked;
	const minuscule = pw_lettres_minuscule.checked;
	const number = pw_nombres.checked;
	const speciaux = pw_caracteres_speciaux.checked;
	const password_final = generer_passWord(majuscule,minuscule,number,speciaux,taille_password);

	resultat_pw.innerText = password_final;
	


});
