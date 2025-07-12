// Configuración de Supabase
const SUPABASE_URL = 'https://rnxlymutkzygnqwbnhtj.supabase.co';
const SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJueGx5bXV0a3p5Z25xd2JuaHRqIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MjExMzg2MywiZXhwIjoyMDY3Njg5ODYzfQ.OYr4GuULELKXxVgmYsp2830-QY1vYlB3v7iwLiuRSAk';
const USERS_TABLE = 'users';

// Función para iniciar sesión
async function loginUser(email, password) {
    console.log('loginUser called with:', { email, password });
    const url = `${SUPABASE_URL}/rest/v1/${USERS_TABLE}?email=eq.${email}`;
    console.log('loginUser fetch URL:', url);
    const headers = {
        apikey: SUPABASE_KEY,
        Authorization: `Bearer ${SUPABASE_KEY}`,
        'Content-Type': 'application/json'
    };
    console.log('loginUser fetch headers:', headers);

    const { data, error } = await fetch(url, {
        headers
    }).then(res => res.json().then(data => ({ data })));

    console.log('loginUser fetch response:', { data, error });

    if (!data || data.length === 0) {
        alert('Usuario no encontrado');
        return false;
    }
    if (data[0].password !== password) {
        alert('Contraseña incorrecta');
        return false;
    }
    alert('¡Bienvenido!');
    // Aquí puedes redirigir o guardar sesión
    return true;
}

// Función para registrar usuario
async function registerUser(email, password, confirmPassword) {
    console.log('registerUser called with:', { email, password, confirmPassword });
    if (password !== confirmPassword) {
        alert('Las contraseñas no coinciden');
        return false;
    }
    // Verifica si el correo ya existe
    const urlCheck = `${SUPABASE_URL}/rest/v1/${USERS_TABLE}?email=eq.${email}`;
    const headers = {
        apikey: SUPABASE_KEY,
        Authorization: `Bearer ${SUPABASE_KEY}`,
        'Content-Type': 'application/json'
    };
    console.log('registerUser check fetch URL:', urlCheck);
    console.log('registerUser check fetch headers:', headers);

    const { data } = await fetch(urlCheck, {
        headers
    }).then(res => res.json().then(data => ({ data })));

    console.log('registerUser check fetch response:', data);

    if (data && data.length > 0) {
        alert('El correo ya está registrado');
        return false;
    }

    // Registra el usuario
    const urlRegister = `${SUPABASE_URL}/rest/v1/${USERS_TABLE}`;
    const body = JSON.stringify({ email, password });
    console.log('registerUser register fetch URL:', urlRegister);
    console.log('registerUser register fetch headers:', headers);
    console.log('registerUser register fetch body:', body);

    const { error } = await fetch(urlRegister, {
        method: 'POST',
        headers,
        body
    }).then(res => res.json());

    console.log('registerUser register fetch response:', { error });

    if (error) {
        alert('Error al registrar usuario');
        return false;
    }
    alert('Usuario registrado correctamente');
    return true;
}

