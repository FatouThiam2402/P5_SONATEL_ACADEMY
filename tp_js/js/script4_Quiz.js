const tab_questions = [

	{
		question: "Quel est le Meilleur Langage de Programmation en 2022",
		a: "Java",
		b: "C",
		c: "Python",
		d: "JavaScript",
		correct: "d"
	},
	{
		question: "Quel est le  Langage de Programmation le plus utilisé en 2023",
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
			console.log(Object.keys(element)[j]);
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
	button.type = "submit";
	button.textContent = "Suivant";
	
	form.appendChild(button); 	
	div_quiz.appendChild(form);
	i += 1;
	

});