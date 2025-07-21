// URL base de JSON Server para tareas
const TODO_URL = 'http://localhost:3000/to-do';

// Crear una nueva tarea (POST /to-do)
export async function createToDo(title) {
    const newTodo = { title, completed: false };
    const response = await fetch(TODO_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(newTodo)
    });
    if (!response.ok) {
        alert('Error al crear la tarea');
        return null;
    }
    const todo = await response.json();
    alert('Tarea creada correctamente');
    return todo;
}

// Leer todas las tareas (GET /to-do)
export async function getToDo() {
    const response = await fetch(TODO_URL);
    if (!response.ok) {
        alert('Error al obtener las tareas');
        return [];
    }
    const todos = await response.json();
    return todos;
}

// Editar una tarea (PATCH /to-do/:id)
export async function updateToDo(id, updatedFields) {
    const response = await fetch(`${TODO_URL}/${id}`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(updatedFields)
    });
    if (!response.ok) {
        alert('Error al actualizar la tarea');
        return null;
    }
    const todo = await response.json();
    alert('Tarea actualizada correctamente');
    return todo;
}

// Borrar una tarea (DELETE /to-do/:id)
export async function deleteToDo(id) {
    const response = await fetch(`${TODO_URL}/${id}`, {
        method: 'DELETE'
    });
    if (!response.ok) {
        alert('Error al borrar la tarea');
        return false;
    }
    alert('Tarea eliminada correctamente');
    return true;
}