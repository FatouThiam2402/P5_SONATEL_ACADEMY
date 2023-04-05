

setInterval(() =>{


function getSecondes(date){

	const secondes = Math.floor(date / 1000);
	const mili = date % 1000;
	return [secondes,mili];
}


function getJours(secondes){

	const jours = Math.floor(secondes/86400);
	const restes_jours = secondes % 86400;

	return [jours,restes_jours];
}

function getHeures(restes_jours){

	const heures = Math.floor(restes_jours / 3600);
	const restes_heures = restes_jours % 3600;

	return [heures,restes_heures]
}


function getMinutes(restes_heures){

	const minutes = Math.floor(restes_heures / 60);
	const restes_minutes = restes_heures % 60;

	return [minutes,restes_minutes];
}





// convertir la date en milliseconde
const milli_seconde_actuelle = new Date().getTime();


// Date actuelle  
const [seconde_actuelle,mili] = getSecondes(milli_seconde_actuelle);


const [jours,restes_jours] = getJours(seconde_actuelle);


const [heures,restes_heures] = getHeures(restes_jours);


const [minutes,restes_minutes] = getMinutes(restes_heures);



// Date À Venir

// date en 2024
const date_en_2024 = new Date("janvier 1, 2024 0:0:0");

const seconde_en_2024 = date_en_2024.getTime();
//console.log("2024",seconde_en_2024)

const [seconde_2024,milli] = getSecondes(seconde_en_2024);

const [jours_2024,restes_jours_2024] = getJours(seconde_2024);



const [heures_2024,restes_heures_2024] = getHeures(restes_jours_2024);



const [minutes_2024,restes_minutes_2024] = getMinutes(restes_heures_2024);



// difference entre les Dates

const jourss = document.getElementById("jours");

const h1_j = jourss.querySelector("h1");
const h3 = jourss.querySelector("h3");

const heuress = document.getElementById("heurs");
const h1_h = heuress.querySelector("h1");
const minutess = document.getElementById("minutes");
const h1_m = minutess.querySelector("h1");
const secondess = document.getElementById("secondes");
const h1_s = secondess.querySelector("h1");

const jours_dif = jours_2024 - jours;
const heure_dif = heures_2024 - heures;
const minutes_dif = minutes_2024 - minutes;
const secondes_dif = restes_minutes_2024 - restes_minutes;

h1_j.textContent = jours_dif;
h1_h.textContent = heure_dif;
h1_m.textContent = minutes_dif;
h1_s.textContent = secondes_dif;



},1000);




