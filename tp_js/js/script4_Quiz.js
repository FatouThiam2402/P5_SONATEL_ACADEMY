const tab_questions = [

	{
		question: "Quel est la Meilleur Langage de Programmation en 2022",
		a: "Java",
		b: "C",
		c: "Python",
		d: "JavaScript",
		correct: "d"
	},
	{
		question: "Quel est la  Langage de Programmation le plus utilisé en 2023",
		a: "Java",
		b: "C",
		c: "Python",
		d: "JavaScript",
		correct: "c"
	},
	{
		question: "Quelle est la syntaxe du langage de programmation et est-elle facile à apprendre et à utiliser ?",
		a: "Java",
		b: "C",
		c: "Python",
		d: "JavaScript",
		correct: "c"
	},
	{
		question: "Qui a crée le Langage Python ?",
		a: "Guido van Rossum",
		b: "Brendan Eich",
		c: "Dennis Ritchie",
		d: "James Gosling",
		correct: "a"
	},
	{
		question: "En quelle année JavaScript a été creer?",
		a: "1989",
		b: "1995",
		c: "1987",
		d: "2000",
		correct: "b"
	},
	];
// Object.keys() donne les clés de l'objet
// Object.keys(element)[0] affiche la premiere clé

let i = 1;
tab_questions.forEach(element =>{	
	
	const h1 = document.createElement("h1");
	h1.textContent = element['question'];
	const div_quiz = document.getElementById("the_quiz");
	
			
	const form = document.createElement("form");
	form.className = "question"+i;
	form.appendChild(h1);
	for(let j = 1; j < Object.keys(element).length -1; j += 1){
			
			const input = document.createElement("input");
			input.type = "radio"
			input.name = "myRadio"
			const label = document.createElement("label");
			label.textContent = element[Object.keys(element)[j]];
			form.appendChild(input);
			form.appendChild(label);
			const br = document.createElement("br");
			form.appendChild(br);

			
		}
	const br = document.createElement("br");
	form.appendChild(br);
	const input = document.createElement("input");
	const button = document.createElement("Button");
	button.type = "button";
	button.textContent = "Suivant";
	// ajouter une classe au niveau de chaque boutton suivant
	button.className = "suivant"+ i;
	
	form.appendChild(button); 	
	div_quiz.appendChild(form);
	i += 1;
	

});


// afficher le premier formulaire et cacher les 4 suivant
const form2 = document.querySelector(".question2");
form2.style = "display:none;"
const form3 = document.querySelector(".question3");
form3.style = "display:none;"
const form4 = document.querySelector(".question4");
form4.style = "display:none;"
const form5 = document.querySelector(".question5");
form5.style = "display:none;"

// je déclare une variable score
var score = 0;
// je recupère le boutton suivant1

let suivant1 = document.querySelector(".suivant1");
suivant1.addEventListener("click",function(){

	const form_suiv = next_form();
		form_suiv.style.display = "block";
		console.log(form_suiv)

});

let suivant2 = document.querySelector(".suivant2");
suivant2.addEventListener("click",function(){

	const form_suiv = next_form();
		form_suiv.style.display = "block";
		console.log(form_suiv)

});



// fonction pour afficher le prochain formulaire
function next_form(){
	const les_forms = document.getElementsByTagName("form"); // recupèrer tous les forms
	const form_actif = document.querySelector('form:not([style="display: none;"])');// recupère le form actif
	form_actif.style.display = "none"; // désactiver le form actif

	for (let i = 0; i < les_forms.length; i+=1){
		if(les_forms[i] === form_actif){

			console.log(form_actif);
			
		}
		else{
			return "vous avez terminer";
		}
		
	}

}


