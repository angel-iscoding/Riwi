import localStorage from "../../scripts/utils/localStorage.js";
import userController from "../../scripts/userController.js";
import eventController from "../../scripts/eventController.js";
import redirect from "../../scripts/utils/redirect.js";

try {
    const addEventBtn = document.querySelector('.add-event-btn');
    const local = localStorage.getItems(["email", "password"]);
    const user = await userController.getUserByEmail(local[0]);
    
    if (!local.every(element => element !== null)) { 
        alert("You're not logged");
        redirect("/src/index.html");
    }
    if (!user)  {
        alert("User not exist");
        redirect("/src/index.html");    
    }
    if (user.email !== local[0] || user.password !== local[1]) { 
        alert("Invalid credentials");
        redirect("/src/index.html");    
    }

    // Renderiza datos del usuario en el sidebar
    document.querySelector('.profile-name').textContent = user.nickname;
    document.querySelector('.profile-role').textContent = user.isAdmin ? "Admin" : "Guest";

    // Renderiza eventos
    const events = await eventController.getEvents();
    const eventsContainer = document.getElementById("events-container");
    eventsContainer.innerHTML = ""; // Limpia el contenedor

    // Formato de fecha como en la imagen: 08-Dec, 2021
    function formatDate(dateStr) {
        if (!dateStr) return "";
        // Si ya está en formato correcto, retorna igual
        if (/\d{2}-[A-Za-z]{3}, \d{4}/.test(dateStr)) return dateStr;
        const date = new Date(dateStr);
        if (isNaN(date)) return dateStr;
        const day = String(date.getDate()).padStart(2, '0');
        const month = date.toLocaleString('en-US', { month: 'short' });
        const year = date.getFullYear();
        return `${day}-${month}, ${year}`;
    }

    if (!user.isAdmin) {
        addEventBtn.style.display = 'none';
    }

    events.forEach(event => {
        const row = document.createElement("div");
        row.className = "event-row";
        row.innerHTML = `
            <div class="event-cell"><img src="../../images/event.jpg" alt="Event" class="event-img"></div>
            <div class="event-cell">${event.title || ""}</div>
            <div class="event-cell">${event.description || ""}</div>
            <div class="event-cell">${event.capacity || 12}</div>
            <div class="event-cell">${formatDate(event.date) || "08-Dec, 2021"}</div>
            <div class="event-cell event-actions">
                <span class="icon" title="Edit">&#9998;</span>
                <span class="icon" title="Delete">&#128465;</span>
            </div>
        `;
        eventsContainer.appendChild(row);
    });

    document.getElementById("Signout").addEventListener('click', (event) => {
        event.preventDefault();

        localStorage.clear();
        redirect("/src/index.html");
    });
} catch (error) {
    alert(error)
}

