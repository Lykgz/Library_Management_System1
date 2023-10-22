// script.js

// Function to confirm book deletion
function confirmDelete() {
    return confirm("Are you sure you want to delete this book?");
}

// Attach the confirmation to the delete links
const deleteLinks = document.querySelectorAll('.delete-link');
deleteLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        if (!confirmDelete()) {
            e.preventDefault();
        }
    });
});
