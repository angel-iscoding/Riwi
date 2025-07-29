import localStorage from "../utils/localStorage.js";
import redirect from "../utils/redirect.js";
import userController from "../userController.js";
import categoriesController from "../categoriesController.js";
import isEmpty from "../utils/isEmpty.js";

const id = localStorage.getItem("id")

if (!id) redirect("index.html");
if (!await userController.thisIdExist(id)) redirect("index.html");

const categoriesDiv = document.getElementById('categories');

const categories = (await categoriesController.getCategories()).map(element => element.name);
if (categories.length > 0) createCategories(categories);

document.querySelector('form').addEventListener('submit', async () => {
    const name = document.getElementById('name').value;

    if (!name) {
        alert('You cant post null values');
        return false
    }


    if (isEmpty({name})) {
        alert('You cant send empty values');
        return false
    }

    categoriesController.postCategory({name}); 
    alert('Category created!')

    categoriesDiv.innerHTML = ''
    createCategories(await categoriesController.getCategories()).map(element => element.name)
})


function createCategories (categories) {
    categories.forEach(element => {

    const newDiv = document.createElement('div');

    const name = document.createElement('p');
    const actions = document.createElement('div');

    const editBtn = document.createElement('button');
    const deleteBtn = document.createElement('button'); 

    name.textContent = element;
    editBtn.textContent = 'Edit';
    deleteBtn.textContent = 'Delete'; 
    
    actions.appendChild(editBtn);
    actions.appendChild(deleteBtn);

    newDiv.appendChild(name);
    newDiv.appendChild(actions);

    categoriesDiv.appendChild(newDiv)

    });
}

