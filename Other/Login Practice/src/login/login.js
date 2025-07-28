import { loginUser } from "../script.supabase.js";
import { loginUserLocal } from "../script.local.js";

document.querySelector('form').addEventListener('submit', async function(e) {
    e.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    await loginUserLocal(email, password);
});