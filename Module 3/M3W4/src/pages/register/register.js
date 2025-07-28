import generateSHA256 from "../../scripts/utils/generateHash.js";
import isEmpty from "../../scripts/utils/isEmpty.js";
import isEmail from "../../scripts/utils/isEmail.js";
import userController from "../../scripts/userController.js"

document.querySelector("form").addEventListener("submit", async (event) => {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const nickname = document.getElementById("nickname").value;
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirmPassword").value;    

    if (email === null) {
        alert("You can't send a null value");
        return false;
    }

    if (nickname === null) {
        alert("You can't send a null value");
        return false;
    }
    
    if (password === null) {
        alert("You can't send a null value");
        return false;
    }

    if (confirmPassword === null) {
        alert("You can't send a null value");
        return false;
    }
    
    if (isEmpty({ email, nickname, password, confirmPassword })) {
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

    const hashedPassword = generateSHA256(password);
    const hashedConfirmPassword = generateSHA256(confirmPassword);

    if (!hashedPassword !== hashedConfirmPassword) {
        alert("The passwords isn't equal")
        return false;
    }

    try {
        const response = await userController.postUser({nickname, email, hashedPassword, isAdmin: false});
        alert(response)
    } catch (error) {
        console.log("Error: " + error);
    }
    
});