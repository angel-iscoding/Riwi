// Configuración de Supabase
const URL = 'https://qmcvwjhihwuoepzcprmv.supabase.co/rest/v1/users';
const API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFtY3Z3amhpaHd1b2VwemNwcm12Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MjcxMzIyNywiZXhwIjoyMDY4Mjg5MjI3fQ.wHepnufDopMGzpVrk86-q4oN8W27rEmuNdmSJyE7Xos';

// Función para iniciar sesión 
export async function loginUser(email, password) {
    // Creamos la URL para buscar el usuario por email
    const url = URL + '?email=eq.' + email;

    // Creamos los headers necesarios
    const headers = {
        apikey: API_KEY,
        Authorization: 'Bearer ' + API_KEY,
        'Content-Type': 'application/json'
    };

    // Hacemos la petición para buscar el usuario
    const response = await fetch(url, { headers: headers });
    const data = await response.json();

    console.log(data);

    // Si no encontramos el usuario
    if (!data || data.length === 0) {
        alert('Usuario no encontrado');
        return false;
    }

    // Si la contraseña no coincide
    if (data[0].password !== password) {
        alert('Contraseña incorrecta');
        return false;
    }

    // Si todo está bien
    alert('¡Bienvenido!');
    return true;
}

// Función para registrar usuario 
export async function registerUser(email, password, confirmPassword) {
    // Verificamos que las contraseñas coincidan
    if (password !== confirmPassword) {
        alert('Las contraseñas no coinciden');
        return false;
    }

    // Revisamos si el correo ya existe
    const url = URL + '?email=eq.' + email;
    const headers = {
        apikey: API_KEY,
        Authorization: 'Bearer ' + API_KEY,
        'Content-Type': 'application/json'
    };

    const responseCheck = await fetch(url, { headers: headers });
    const dataCheck = await responseCheck.json();

    if (dataCheck && dataCheck.length > 0) {
        alert('El correo ya está registrado');
        return false;
    }

    // Registramos el usuario
    const urlRegister = URL;
    const body = JSON.stringify({ email: email, password: password });

    const responseRegister = await fetch(urlRegister, {
        method: 'POST',
        headers: headers,
        body: body
    });

    // Si hay error al registrar
    if (!responseRegister.ok) {
        alert('Error al registrar usuario');
        return false;
    }

    alert('Usuario registrado correctamente');
    return true;
}