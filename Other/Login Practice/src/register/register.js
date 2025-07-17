import { registerUser } from "../script.supabase.js";

document.querySelector('form').addEventListener('submit', async function(e) {
    e.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm-password').value;

    await registerUser(email, password, confirmPassword);
});