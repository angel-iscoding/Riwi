import userController from '../userController.js'
import isEmpty from '../utils/isEmpty.js';
import isEmail from '../utils/isEmail.js';
import generateSHA256 from '../utils/generateHash.js';
import redirect from '../utils/redirect.js';
import localStorage from '../utils/localStorage.js';

const id = localStorage.getItem("id")

if (!await userController.thisIdExist(id)) localStorage.clear();
else redirect("/src/pages/dashboard.html");

document.querySelector('form').addEventListener('submit', async (event) => {
    try {
        event.preventDefault();
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        if (email === null || password === null) {
            alert ("You can't send a null value");
            return false;
        }

        if (isEmpty({ email, password })) {
            alert("You can't send empty values");
            return false;
        } 
        if (!isEmail(email)) {
            alert("You need to send a valid email");
            return false;
        }

        const user = await userController.getUserByEmail(email);

        if (!user) {
            alert("Usuario no encontrado");
            return false;
        }

        if (user.password !== generateSHA256(password)) {
            alert("The password is not correct");
            return false;
        }
        localStorage.setStorage({id: user.id});
        redirect("src/pages/dashboard.html");
    } catch (error) {
        alert("Ha ocurrido un error inesperado.\n" + error)
    }     
})