<script type="text/javascript">

			/*function ajoutContener()
			{*/
				const ajoutBoutton = document.querySelector('#ajout');
				ajoutBoutton.addEventListener('click',function(){
					const carte = document.createElement("div");
					carte.classList.add('sous_contener');
					
					let header = document.createElement("header");
					let icons = document.createElement("div");
					let img1 = document.createElement("img");
					let img2 = document.createElement("img");

					img1.src = "../images/modifier.svg";
					img2.src = "../images/corbeille.svg";
					img1.alt = "modifier";
					img2.alt = "corbeille";
					img2.classList.add('id_image2');
					icons.appendChild(img1);
					icons.appendChild(img2);
					header.appendChild(icons);
					const ajoutBoutton = document.querySelector('.id_image2');
					const textarea = document.createElement("textarea");
					carte.appendChild(header);
					carte.appendChild(textarea);
					const cartes = document.getElementById("contener1");
					const listes_cartes = document.querySelectorAll('sous_contener');
					cartes.appendChild(carte);
					const contene = document.getElementById('contener');
					contene.appendChild(cartes);
					

				});
				img2.addEventListener('click',function(){
						removeChild(cartes,carte);
					});


				/*const header = document.createElement("header");
				const textarea = document.createElement("textarea");
				const carte = document.createElement("div");



				const sous_contener = document.getElementById('sous_contener');
				const contener1 = document.getElementById("contener1");
				const contener = document.getElementById('contener');
				
				
				header.className = 'header'
				textarea.className = 'textarea'
				sous_contener.className = 'sous_contener'
				
				sous_contener.appendChild(header);
				sous_contener.appendChild(textarea);

				contener1.appendChild(sous_contener);

				contener.appendChild(contener1);*/
				
				
		/*	}*/
			/*let add_note = getElementById("ajout");
			add_note.addEventListener('click',ajoutContener());*/
			


		</script>