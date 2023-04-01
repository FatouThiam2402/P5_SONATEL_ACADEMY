const div_gauche = document.querySelector(".div_gauche");
let tab =  new Array("Mon Premier","Mon deuxieme","Mon troisieme","Mon Quatrieme");

const bouton_vers_droite = document.getElementById("boutton_droite");
const bouton_vers_gauche = document.getElementById("boutton_gauche");
const div_droite = document.querySelector(".div_droite");

tab.forEach(function(elemt){

const paragraph = document.createElement("p");
paragraph.textContent = elemt;

div_gauche.appendChild(paragraph);
paragraph.addEventListener("mouseover",function(){
	paragraph.classList.add("selected");
})

})

function actif_or_desactif_bouton(){
	

	if (div_gauche.children.length == 0){
		bouton_vers_droite.disabled = true	
		bouton_vers_droite.style.background = "red"
	}
	else{
		bouton_vers_droite.disabled = false	
		bouton_vers_droite.style.background = "green"
	}

	if (div_droite.children.length == 0){
		bouton_vers_gauche.disabled = true	
		bouton_vers_gauche.style.background = "red"
	}
	else{
		bouton_vers_gauche.disabled = false	
		bouton_vers_gauche.style.background = "green"
	}

}


actif_or_desactif_bouton()


bouton_vers_droite.addEventListener("click",function(){
	const p = div_gauche.querySelector(".selected");
	div_droite.appendChild(p);
	actif_or_desactif_bouton()	
})

bouton_vers_gauche.addEventListener("click",function(){
	const p_selected = div_droite.querySelector(".selected");
	div_gauche.appendChild(p_selected);
	actif_or_desactif_bouton()

})

