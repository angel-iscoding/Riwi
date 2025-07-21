# Entrenamiento - M3S3: Interacción con servidores y Consumo de APIs

## Descripción

Este proyecto es una aplicación web de lista de tareas (To-Do App) desarrollada como ejercicio de entrenamiento y estudio para la semana 3 del módulo 3 de Riwi. El objetivo principal es practicar la interacción con servidores y el consumo de APIs utilizando JavaScript moderno y JSON Server como backend simulado.

## Funcionalidad

- **Agregar tareas:** Permite crear nuevas tareas que se almacenan en el servidor.
- **Listar tareas:** Muestra todas las tareas almacenadas, indicando si están completadas o no.
- **Editar tareas:** Permite modificar el título de una tarea existente.
- **Completar/desmarcar tareas:** Permite marcar una tarea como completada o pendiente.
- **Eliminar tareas:** Permite borrar tareas de la lista y del servidor.

Todas las operaciones se realizan mediante peticiones HTTP (`GET`, `POST`, `PATCH`, `DELETE`) a un servidor local simulado con JSON Server.

## ¿Cómo se hizo?

- **Frontend:** HTML, CSS y JavaScript puro (sin frameworks).
- **Backend simulado:** [JSON Server](https://github.com/typicode/json-server) para simular una API RESTful.
- **Lógica de interacción:** Toda la lógica para consumir la API está en [`server/interaccionConServidores.js`](server/interaccionConServidores.js).
- **Interfaz:** El archivo [`index.html`](index.html) contiene la estructura y [`styles.css`](styles.css) el diseño visual.

## Cómo ejecutar el proyecto

1. **Instala JSON Server** (si no lo tienes):
   ```sh
   npm install -g json-server

2. Inicia le servidor JSON Server. Desde la raíz del proyecto. Ejecuta: 

```cmd
json-server --watch server/to-do.json --port 3000
```

Esti levantará un servidor en http://localhost:3000/to-do.

3. Abre la aplicación web: Abre [`index.html`](index.html) en tu navegador. La aplicación se conectará automáticamente al servidor JSON Server para mostrar y gestionar las tareas.