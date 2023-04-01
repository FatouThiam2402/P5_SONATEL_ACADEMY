
		const projet = document.querySelector(".mon_projet");
		const bouton_succes = document.querySelector(".succes");
		

		bouton_succes.addEventListener("click",function(){
			const paragraph =  document.createElement("p");
			paragraph.textContent = "Mon Projet 4";
			projet.appendChild(paragraph);
			projet.style.backgroundColor = "green";

			projet.style.display = "block";
			setTimeout(function(){
				projet.style.display = "none"
			},1000)


		})

		const bouton_danger = document.querySelector(".danger");
		

		bouton_danger.addEventListener("click",function(){
			const paragraph =  document.createElement("p");
			paragraph.textContent = "Mon Projet 4";
			projet.appendChild(paragraph);
			projet.style.backgroundColor = "red";

			projet.style.display = "block";
			setTimeout(function(){
				projet.style.display = "none"
			},1000)


		})

		const bouton_warning = document.querySelector(".warning");
		

		bouton_warning.addEventListener("click",function(){
			const paragraph =  document.createElement("p");
			paragraph.textContent = "Mon Projet 4";
			projet.appendChild(paragraph);
			projet.style.backgroundColor = "yellow";

			projet.style.display = "block";
			setTimeout(function(){
				projet.style.display = "none"
			},1000)


		})

		const bouton_info = document.querySelector(".info");
		

		bouton_info.addEventListener("click",function(){
			const paragraph =  document.createElement("p");
			paragraph.textContent = "Mon Projet 4";
			projet.appendChild(paragraph);
			projet.style.backgroundColor = "aqua";

			projet.style.display = "block";
			setTimeout(function(){
				projet.style.display = "none"
			},1000)


		})
		
		
	