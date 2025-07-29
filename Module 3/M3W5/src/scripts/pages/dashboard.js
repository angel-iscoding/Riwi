import localStorage from "../utils/localStorage.js";
import redirect from "../utils/redirect.js";
import userController from "../userController.js";
import operationsController from "../operationsController.js";
import categoriesController from "../categoriesController.js"

const id = localStorage.getItem("id")

if (!id) redirect("index.html");
if (!await userController.thisIdExist(id)) redirect("index.html");

const operations = await operationsController.getOperationsOfUserId(id);
const categories = (await categoriesController.getCategories()).map(element => element.name);

const selectCategories = document.getElementById("category");
const operationsElement = document.getElementById("elements");
const newOperationBtn = document.getElementById("operationBtn");

const enarnings = document.getElementById('earnings-p');
const bills = document.getElementById('bills-p');
const total = document.getElementById('total-p');

document.getElementById('sign-out').addEventListener('click', () => {
    localStorage.clear();
    redirect('index.html');
})

let totalRevenues = 0;
let totalSpents = 0;


if (categories.length > 0) categories.forEach(element => createCategoriesSelectors(element));
if (operations) {    
    createOperationsElements(operations);

    operations.forEach((element) => {
        if (element.type === "revenue") totalRevenues+=element.amount;
        if (element.type === "spent") totalSpents-=element.amount;
    });

    enarnings.textContent = String(totalRevenues);
    bills.textContent = String(totalSpents);

    total.textContent = (totalRevenues + totalSpents);
}

newOperationBtn.addEventListener('click', redirectNewOperation);

function redirectNewOperation () {
    redirect("src/pages/operation.html")
}


export function createCategoriesSelectors (element){
    const newOption = document.createElement('option');

    newOption.setAttribute('value', element);
    newOption.textContent = element;

    selectCategories.appendChild(newOption);
} 

function createOperationsElements (operations) {
    operations.forEach((element) => {
        const newDiv = document.createElement('div');
        newDiv.setAttribute('id', element.id)

        const description = document.createElement('p');
        const category = document.createElement('p');
        const date = document.createElement('p');
        const amount = document.createElement('p');
        const actions = document.createElement('div');

        const editBtn = document.createElement('button');
        const deleteBtn = document.createElement('button'); 

        description.textContent = element.description;
        category.textContent = element.category;
        date.textContent = element.date;
        amount.textContent = element.amount;

        editBtn.textContent = 'Edit';
        deleteBtn.textContent = 'Delete'; 
        
        actions.appendChild(editBtn);
        actions.appendChild(deleteBtn);

        newDiv.appendChild(description);
        newDiv.appendChild(category);
        newDiv.appendChild(date);
        newDiv.appendChild(amount);
        newDiv.appendChild(actions);
        operationsElement.appendChild(newDiv);
    })
}

// Dashboard URL http://127.0.0.1:5500/src/pages/Dashboard/dashboard.html
