const URL = "https://rickandmortyapi.com/api/character" 

const data = await fetch(URL)
    .then(results => results.json())

console.log(data.results);

const container = document.getElementById("data")
console.log(container);

data.results.forEach(element => {
    const mainDiv = document.createElement("div");
    mainDiv.classList.add('card');

    //Contenedores
    const aside = document.createElement('aside');
    const section = document.createElement('section');

    aside.classList.add('cartAside')
    aside.style.backgroundImage = `url(${element.image})`

    //Informacion
    const name = document.createElement('h3');
    name.textContent = element.name
    
    const info = document.createElement('p');
    
    //Titulos
    const titleLocation = document.createElement('h4');
    const location = document.createElement('p');
    
    const titleOrigin = document.createElement('h4');
    const origin = document.createElement('p');

    section.appendChild(name)

    //Agregar contendores
    mainDiv.appendChild(aside);
    mainDiv.appendChild(section);

    container.appendChild(mainDiv);
});