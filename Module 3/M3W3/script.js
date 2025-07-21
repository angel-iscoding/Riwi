import { createToDo, getToDo, updateToDo, deleteToDo } from './server/interaccionConServidores.js';

const todoForm = document.getElementById('todo-form');
const todoTitleInput = document.getElementById('todo-title');
const todoList = document.getElementById('todo-list');

//todo json-server --watch to-do.json --port 3000


// Renderizar todas las tareas
async function renderTodos() {
    todoList.innerHTML = '';
    const todos = await getToDo();
    todos.forEach(todo => {
        const li = document.createElement('li');
        li.className = 'todo-item' + (todo.completed ? ' completed' : '');
        li.dataset.id = todo.id;

        const spanTitle = document.createElement('span');
        spanTitle.className = 'todo-title';
        spanTitle.textContent = todo.title;

        const actions = document.createElement('span');
        actions.className = 'todo-actions';

        // Botón completar
        const completeBtn = document.createElement('button');
        completeBtn.className = 'complete-btn';
        completeBtn.textContent = todo.completed ? 'Desmarcar' : 'Completar';
        completeBtn.onclick = async () => {
            await updateToDo(todo.id, { completed: !todo.completed });
            renderTodos();
        };

        // Botón editar
        const editBtn = document.createElement('button');
        editBtn.className = 'edit-btn';
        editBtn.textContent = 'Editar';
        editBtn.onclick = () => {
            const nuevoTitulo = prompt('Nuevo título:', todo.title);
            if (nuevoTitulo && nuevoTitulo.trim() !== '') {
                updateToDo(todo.id, { title: nuevoTitulo }).then(renderTodos);
            }
        };

        // Botón eliminar
        const deleteBtn = document.createElement('button');
        deleteBtn.className = 'delete-btn';
        deleteBtn.textContent = 'Eliminar';
        deleteBtn.onclick = async () => {
            if (confirm('¿Seguro que quieres eliminar esta tarea?')) {
                await deleteToDo(todo.id);
                renderTodos();
            }
        };

        actions.appendChild(editBtn);
        actions.appendChild(deleteBtn);
        actions.appendChild(completeBtn);

        li.appendChild(spanTitle);
        li.appendChild(actions);

        todoList.appendChild(li);
    });
}

// Agregar nueva tarea
todoForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const title = todoTitleInput.value.trim();
    if (title) {
        await createToDo(title);
        todoTitleInput.value = '';
        renderTodos();
    }
});

// Inicializar
renderTodos();