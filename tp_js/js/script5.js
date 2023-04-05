const APIURL ="https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=04c35731a5ee918f014970082a0088b1&page=1";
const IMGPATH = "https://image.tmdb.org/t/p/w200";
const SEARCHAPI =
"https://api.themoviedb.org/3/search/movie?&api_key=04c35731a5ee918f014970082a0088b1&query=";


fetch(APIURL)
.then(response => response.json())
.then(data => {
    const dict_results = data["results"];
    const contener = document.getElementById("contener");
    const entete = document.getElementById("rechercher");
    const films = document.getElementById("films"); //original_title, overview , vote_average
    console.log(dict_results);
    dict_results.forEach ( element =>{                              // img.src = IMGPATH+element.poster_path
        

        const film = document.createElement("div");
        const img = document.createElement("img");

        //const src = document.createAttribute('src');
        img.setAttribute("src",IMGPATH+element["poster_path"]);       // img.src = IMGPATH+element.poster_path
        film.appendChild(img);
        films.appendChild(film);

       
        const div_footer = document.createElement("div");
         const h3 = document.createElement("h3");

        contener.appendChild(entete);
        contener.appendChild(films);

    });

});
.catch(error => console.error(error));




