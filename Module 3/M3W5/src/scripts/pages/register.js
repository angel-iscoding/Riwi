import generateSHA256 from "../utils/generateHash.js";
import isEmpty from "../utils/isEmpty.js";
import isEmail from "../utils/isEmail.js";
import userController from "../userController.js";

document.querySelector("form").addEventListener("submit", async (event) => {
    try {
        event.preventDefault();

        const email = document.getElementById("email").value;
        const name = document.getElementById("name").value;
        const password = document.getElementById("password").value;
        const confirmPassword = document.getElementById("confirmPassword").value;    

        if (email === null || name === null || password === null || confirmPassword === null) {
            alert("You can't send a null value");
            return false;
        }

        if (isEmpty({ email, name, password, confirmPassword })) {
            alert("The fields cannot be empty")
            return false;
        }

        if (password.length < 8) {
            alert("The password must have at least 8 characters")
            return false;
        }

        if (confirmPassword.length < 8) {
            alert("The password must have at least 8 characters")
            return false;
        }

        if (!isEmail(email)) {
            alert("You need to send a valid email");
            return false;
        }

        if (await userController.thisUserExist(email)) {
            alert("This email is alrealy used");
            return false
        }

        const hashedPassword = generateSHA256(password);
        const hashedConfirmPassword = generateSHA256(confirmPassword);

        if (hashedPassword !== hashedConfirmPassword) {
            alert("The passwords don't match")
            return false;
        }
    
        const response = await userController.postUser({name, email, password: hashedPassword});
        alert("New user created!");
        
    } catch (error) {
        console.log("Error: " + error);
    }
    
});