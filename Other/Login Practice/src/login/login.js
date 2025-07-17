import { loginUser } from "../script.supabase.js";

document.querySelector('form').addEventListener('submit', async function(e) {
    e.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    await loginUser(email, password);
});