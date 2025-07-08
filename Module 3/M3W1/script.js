// Get the register button
const btn = document.querySelector('#submit');

// Add click event listener to the button
btn.addEventListener('click', (event) => {
    event.preventDefault(); // Prevent form submission

    // Get the current date and subtract 18 years to get the minimum allowed birthdate
    const date = new Date();
    date.setFullYear(date.getFullYear() - 18);

    // Get the user's entered birthdate
    const userDate = new Date(document.getElementById('date').value);
    const div = document.getElementById("verification");

    // Clear previous messages
    div.innerHTML = "";

    // Create a new div for the message
    const newDiv = document.createElement("div");

    // Check if user is 18 or older
    if (userDate <= date) {
        newDiv.innerText = "Signing up...";
        newDiv.style.color = "green"; // Success message in green
    } else {
        newDiv.innerText = "You must be at least 18";
        newDiv.style.color = "red"; // Error message in red
    }

    // Add the message to the page
    div.appendChild(newDiv);
});