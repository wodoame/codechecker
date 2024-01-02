document.addEventListener("DOMContentLoaded", function() {
    // Select the form and message elements
    const form = document.getElementById("attendee-form");
    const messageElement = document.querySelector(".message");

    // Check if a message exists and is not empty
    if (messageElement && messageElement.textContent.trim() !== "") {
        // Show the message
        messageElement.style.display = "block";

        // Set a timeout to hide the message after 2 seconds
        setTimeout(function() {
            messageElement.style.display = "none";
        }, 2000);
    }

    // Clear the form input on form submission
    form.addEventListener("submit", function(event) {
        // Reset the form
        form.reset();
        event.preventDefault(); // Prevent the form from submitting, if you are not using AJAX.
    });
});
