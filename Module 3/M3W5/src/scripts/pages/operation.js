import localStorage from "../utils/localStorage.js";
import redirect from "../utils/redirect.js";
import userController from "../userController.js";
import categoriesController from "../categoriesController.js"
import operationsController from "../operationsController.js";
import isEmpty from "../utils/isEmpty.js";

const id = localStorage.getItem("id")

if (!id) redirect("index.html");
if (!await userController.thisIdExist(id)) redirect("index.html");

document.querySelector('form').addEventListener('submit', async (event) => {
    event.preventDefault();

    const description = document.getElementById('description').value;
    const amount = document.getElementById('amount').value;
    const selectType = document.getElementById('type');
    const selectCategory = document.getElementById('category');
    const date = document.getElementById('date').value;

    const typeValue = selectType.options[selectType.selectedIndex].value;
    const categoryValue = selectCategory.options[selectCategory.selectedIndex].value;

    if (!description || !amount || !typeValue || !categoryValue || !date) {
        alert('You cant send null values');
        return false
    }

    if (isEmpty({amount, typeValue, categoryValue, date})) {
        alert('You cant send empty inputs');
        return false
    }

    const amountInt = parseFloat(amount)

    if (amountInt == NaN) {
        alert('Send a valid number');
        return false
    }
    

    await operationsController.postOperation(
        {
            description, 
            amount: amountInt,
            type: typeValue,
            category: categoryValue,
            date,
            userId: id});
        })

document.getElementById('cancel').addEventListener('click', () => {
    redirect("src/pages/dashboard.html");
})


const selectCategories = document.getElementById("category");
const categories = (await categoriesController.getCategories()).map(element => element.name);

if (categories.length > 0) categories.forEach(element => createCategoriesSelectors(element));

export function createCategoriesSelectors (element){
    const newOption = document.createElement('option');

    newOption.setAttribute('value', element);
    newOption.textContent = element;

    selectCategories.appendChild(newOption);
} 
