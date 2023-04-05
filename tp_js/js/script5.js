const APIURL ="https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=04c35731a5ee918f014970082a0088b1&page=1";
const IMGPATH = "https://image.tmdb.org/t/p/w1280";
const SEARCHAPI =
"https://api.themoviedb.org/3/search/movie?&api_key=04c35731a5ee918f014970082a0088b1&query=";


fetch(APIURL)
.then(response => response.json())
.then(data => {
    const dict_results = data["results"];
    const contener = document.getElementById("contener");
    const films = document.getElementById("films");
    console.log(dict_results);
    dict_results.forEach ( element =>{
        console.log(element["backdrop_path"]);

        const div = document.createElement("div");
        const img = document.createElement("img");
        const src = document.createElement('src');
        const h3 = document.createElement("h3");

    })
 



})
.catch(error => console.error(error));




