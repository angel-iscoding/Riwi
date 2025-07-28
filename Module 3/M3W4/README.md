# Event Manager - Proyecto de Gestión de Eventos

## Requisitos previos

- [Node.js y npm](https://nodejs.org/) instalados en tu sistema.

## Instalación de json-server

Para simular una API REST y manejar los datos de usuarios y eventos, este proyecto utiliza [json-server](https://github.com/typicode/json-server).

Instala json-server de manera global ejecutando en la terminal:

```bash
npm install -g json-server
```

## Cómo iniciar el servidor

Ubícate en la raíz del proyecto (donde está `database.json`) y ejecuta:

```bash
json-server --watch database.json --port 3000
```

Esto levantará un servidor en `http://localhost:3000` usando los datos de `database.json`.

## Funcionalidades del Proyecto

### 1. Registro de usuarios
- Los usuarios pueden registrarse proporcionando nickname, email y contraseña.
- La contraseña debe tener al menos 8 caracteres y se almacena encriptada (SHA256).
- Se valida que el email tenga formato correcto y que los campos no estén vacíos.

### 2. Login
- Los usuarios pueden iniciar sesión con su email y contraseña.
- Si las credenciales son correctas, se redirige al dashboard.
- Se utiliza localStorage para mantener la sesión.

### 3. Dashboard
- Visualización de eventos en una tabla.
- El nombre y rol del usuario se muestran en el sidebar.
- Los usuarios con rol de **Admin** pueden ver el botón para agregar nuevos eventos.
- Los usuarios tipo **Guest** solo pueden visualizar los eventos.
- Permite cerrar sesión (logout), limpiando el localStorage y redirigiendo al login.

### 4. Gestión de eventos
- Los eventos se obtienen y gestionan a través de la API simulada por json-server.
- Los administradores pueden agregar, editar y eliminar eventos (funcionalidad visible solo para admins).

### 5. Validaciones y seguridad
- Validación de campos vacíos y formato de email en formularios.
- Contraseñas encriptadas antes de enviarse al backend.
- Redirección automática si el usuario no está autenticado.

---

¡Listo! Ahora puedes iniciar el servidor y probar la aplicación accediendo a los archivos HTML desde tu navegador.
