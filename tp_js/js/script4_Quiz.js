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
			input.value = element[Object.keys(element)[j]];
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
// dans cette div on va ajoute le score et le boutton Rejouer

var div_score = document.getElementById("score");
const input = document.createElement("input");
const h1 = document.createElement("h1");
h1.className = "afficher_score"
input.type = "button";
input.value = "Rejouer";
input.className = "input_rejouer"
div_score.appendChild(h1);
div_score.appendChild(input);



// afficher le premier formulaire et cacher les 4 suivant
const form2 = document.querySelector(".question2");
form2.style = "display:none;"
const form3 = document.querySelector(".question3");
form3.style = "display:none;"
const form4 = document.querySelector(".question4");
form4.style = "display:none;"
const form5 = document.querySelector(".question5");
form5.style = "display:none;"




// fonction pour afficher le prochain formulaire
function next_form(){
	const les_forms = document.getElementsByTagName("form"); // recupèrer tous les forms
	const form_actif = document.querySelector('form:not([style="display: none;"])');// recupère le form actif
	form_actif.style.display = "none"; // désactiver le form actif
	
	for (let i = 0; i < les_forms.length; i+=1){
		if(les_forms[i] === form_actif){

			return les_forms[i+1];
			
		}
		
		
	}

}


// fonction qui permet de retourner la cle si on'a la valeur

function getKeyByValue(object, value) {
  for (let key in object) {
    if (object[key] === value) {
      return key;
    }
  }
  return null;
}



// je déclare une variable score
let score = 0;
// je recupère le boutton suivant1
// je recupere tous les boutton suivant
let btn_suivants = document.getElementsByTagName("button");
for(let i = 1; i < btn_suivants.length+1; i+=1){
	let suivant = document.querySelector(".suivant"+i)
	suivant.addEventListener("click",function(){
	
	const les_forms = document.getElementsByTagName("form"); // recupèrer tous les forms
		const form_actif = document.querySelector('form:not([style="display: none;"])');// recupère le form actif
		const les_choix = form_actif.elements["myRadio"]
		for (let k = 0; k < les_choix.length; k+=1){ // cette boucle permet de calculer le score du questionnaire
			if(les_choix[k].checked){
				const key = getKeyByValue(tab_questions[i-1],les_choix[k].value);
				if(key === tab_questions[i-1]["correct"]){
					score = score + 1;


				}
			}

		}
	
		form_actif.style.display = "none"; 
		for (let j = 0; j < les_forms.length-1; j+=1){
			if(les_forms[j] === form_actif){

				console.log("form suivant",les_forms[j+1]);
				les_forms[j+1].setAttribute("style","display:block");


			}

	

		}
		

		if( score === 0 || score === 1 || score === 2){
			h1.textContent = "Désolé tu peux mieux faire tu as    "+score+"/"+les_forms.length
		}

		if(score === 3){
			h1.textContent = " tu y es presque   "+score+"/"+les_forms.length
		}
		if(score === 4 || score === 5){
			h1.textContent = "Bravo tu as assuré   "+score+"/"+les_forms.length
		}
		
		const fin_suiv = document.querySelector(".suivant"+les_forms.length);
		console.log("5",fin_suiv);

		fin_suiv.addEventListener("click",function(){
			div_score.style.display ="block";

		})
		

	});

	
}




// **************   pourquoi le deuxieme appel de la fonction next_form() ne marche pas  ça marche que sur le premier button suivant  **************** A Revoir *******








