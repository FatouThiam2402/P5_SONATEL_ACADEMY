const APIURL ="https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=04c35731a5ee918f014970082a0088b1&page=100";
const IMGPATH = "https://image.tmdb.org/t/p/w300";
const SEARCHAPI ="https://api.themoviedb.org/3/search/movie?&api_key=04c35731a5ee918f014970082a0088b1&query=";


fetch(APIURL)
.then(response => response.json())
.then(data => {

    const contener = document.getElementById("contener");
    const films = document.getElementById("films"); //original_title, overview , vote_average
    const dict_results = data["results"];

    // c'est une fonction qui permet d'afficher les photos

    const affichage_films = function(element){

        const film = document.createElement("div");
        film.className = "film";
        const img = document.createElement("img");
        img.setAttribute("src",IMGPATH+element["poster_path"]); // img.src = IMGPATH+element.poster_path
        const div_overview = document.createElement("div");// div_overview contient un paragraphe et un div
        div_overview.className = "overview";
        const p_overview = document.createElement("p");
        p_overview.textContent = "Overview:";
        const text_overview = document.createElement("div");
        text_overview.textContent = element["overview"];
        div_overview.appendChild(p_overview);
        div_overview.appendChild(text_overview);

        const div_footer = document.createElement("div");
        div_footer.className = "footer";
        const h3 = document.createElement("h3");
        const p_footer = document.createElement("p");
        h3.textContent = element["original_title"];
        p_footer.textContent = element["vote_average"];
        div_footer.appendChild(h3);
        div_footer.appendChild(p_footer);
        film.appendChild(img);
        film.appendChild(div_footer);
        film.appendChild(div_overview);
        films.appendChild(film);
        contener.appendChild(films);

        var get_overview = document.getElementsByClassName("overview");

        var get_film = document.getElementsByClassName("film");

    }

    
    dict_results.forEach ( element =>{
     
        affichage_films(element);

    });


    /* console.log(get_overview);
    get_film.addEventListener("mouseover",()=>{

    });*/


 /*dict_results.forEach ( element =>{
        element["original_title"].include(valeur_taper);
        affichage_films(element);
    })*/


    const recherche = document.getElementById("button");
    recherche.addEventListener("input",() => {
        const valeur_taper = recherche.value.toLowerCase();
          console.log(valeur_taper);
          films.innerHTML =""
        dict_results.forEach(element =>{
          
            if(element["original_title"].toLowerCase().includes(valeur_taper)){
          
             affichage_films(element); 
            }
            
        })
        
    })





})
.catch(error => console.error(error));




