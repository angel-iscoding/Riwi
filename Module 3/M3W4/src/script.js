import isEmail from "./scripts/utils/isEmail.js";
import isEmpty from "./scripts/utils/isEmpty.js";
import userController from "./scripts/userController.js";
import generateSHA256 from "./scripts/utils/generateHash.js";
import localStorage from "./scripts/utils/localStorage.js";
import redirect from "./scripts/utils/redirect.js";

if (localStorage.getItems(["nickname", "password"]).every(element => element)) {
    redirect("/src/pages/dashboard/dashboard.html");
}

document.querySelector("form").addEventListener("submit", async (event) => {
    try {
        event.preventDefault();

        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;

        if (email === null) {
            alert ("Send a null value");
            return false;
        }

        if (password === null) {
            alert ("Send a null value");
            return false;
        } 
        
        if (isEmpty({ email, password})) {
            alert("You can't send empty values");
            return false;
        } 
        if (!isEmail(email)) {
            alert("You need to send a valid email");
            return false;
        }

        const user = await userController.getUserByEmail(email);
        
        if (user.password !== generateSHA256(password)) {
            alert("The password is not correct");
            return false;
        }        

        localStorage.setStorage(user);
        window.location.href = `${window.location.origin}/src/pages/dashboard/dashboard.html`;
    } catch (error) {
        console.log(error);
    }
});