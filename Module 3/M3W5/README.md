# Módulo 3 - Prueba de desempeño

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

---

¡Listo! Ahora puedes iniciar el servidor y probar la aplicación accediendo a los archivos HTML desde tu navegador.

## Funcionalidades del Proyecto

### 1. Autenticación

-Implementa un formulario de login que permita al usuario iniciar sesión con usuario y contraseña definidos localmente.

-Valida credenciales e iniciar sesión con persistencia el localStorage.

-Permite cerrar sesión desde cualquier punto del sistema.

-Protege las rutas internas de la aplicación: el usuario solo puede acceder al panel de control luego del login exitoso.

### 2. Gestión de operaciones

- Agrega operaciones con los campos: descripción, monto, tipo (gasto o ganancia), categoría y fecha.

- Valida entradas (descripción no vacía, valores nulos).

- Muestra las operaciones en una tabla

### 3. Gestión de categorías

- Agrega categorías.

- Al agregar una categoria, se actualizan los elementos dependientes de esta

### 6. Persistencia de datos

- Guarda estado de sesion en localStorage.

- Restaurar automáticamente al recargar la página.

### 7. Interactividad con el DOM

- Manipula el DOM para actualizar la interfaz de manera dinámica.

### 8. Organización del código

- Separar claramente la lógica de datos, la manipulación del DOM yel control de flujo.

- Evitar duplicación de lógica.


