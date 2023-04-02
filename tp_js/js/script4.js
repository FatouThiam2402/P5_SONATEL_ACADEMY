
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
	String.fromCharCode((Math.floor(Math.random()*26)+65));
}


function generer_pw_lettres_minuscule(){
	String.fromCharCode((Math.floor(Math.random()*26)+97));
}


function generer_pw__chiffres(){
	String.fromCharCode((Math.floor(Math.random()*10)+48));
}


function generer_pw_caracteres_speciaux(){

	const speciaux ="!@#$£%&*(){}[]=<>/,.^"; 

	console.log(speciaux[Math.floor(Math.random()*speciaux.length)]);
	
}



	const taille_password = taille_pw.value;
	const click_majuscule = pw_lettres_majuscule.checked;
	const click_minuscule = pw_lettres_minuscule.checked;
	const click_number = pw_nombres.checked;
	const click_speciaux = pw_caracteres_speciaux.checked;

	const typecontent = click_majuscule + click_minuscule + click_number + click_speciaux;
	const types_arr=[{click_majuscule},{click_minuscule},{click_number},{click_speciaux}];
	console.log(types_arr);

/*console.log(types_arr); voici le resultat ->
0: {click_majuscule: false}
1: {click_minuscule: false}
2: {click_number: false}
3: {click_speciaux: false}
length: 4
*/


btn_generer_passwd.addEventListener("click",function(){

	const taille_password = taille_pw.value;
	const click_majuscule = pw_lettres_majuscule.checked;
	const click_minuscule = pw_lettres_minuscule.checked;
	const click_number = pw_nombres.checked;
	const click_speciaux = pw_caracteres_speciaux.checked;

	const typecontent = click_majuscule + click_minuscule + click_number + click_speciaux;
	const types_arr=[{click_majuscule},{click_minuscule},{click_number},{click_speciaux}];
	console.log(types_arr);


})
