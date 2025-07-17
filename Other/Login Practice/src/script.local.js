// URL base de JSON Server
const LOCAL_URL = 'http://localhost:3000/users';

// Función para iniciar sesión con JSON Server
export async function loginUserLocal(email, password) {
    // Buscamos el usuario por email
    const response = await fetch(`${LOCAL_URL}?email=${email}`);
    const users = await response.json();

    if (!users || users.length === 0) {
        alert('Usuario no encontrado');
        return false;
    }

    if (users[0].password !== password) {
        alert('Contraseña incorrecta');
        return false;
    }

    alert('¡Bienvenido!');
    return true;
}

// Función para registrar usuario con JSON Server
export async function registerUserLocal(email, password, confirmPassword) {
    if (password !== confirmPassword) {
        alert('Las contraseñas no coinciden');
        return false;
    }

    // Revisamos si el correo ya existe
    const response = await fetch(`${LOCAL_URL}?email=${email}`);
    const users = await response.json();

    if (users && users.length > 0) {
        alert('El correo ya está registrado');
        return false;
    }

    // Registramos el usuario
    const newUser = { email, password };
    const registerResponse = await fetch(LOCAL_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newUser)
    });

    if (!registerResponse.ok) {
        alert('Error al registrar usuario');
        return false;
    }

    alert('Usuario registrado correctamente');
    return true;
}