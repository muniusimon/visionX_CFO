document.addEventListener("DOMContentLoaded", function() {
    const headers = document.querySelectorAll("section h3");
    headers.forEach(header => {
        header.addEventListener("click", function() {
            this.nextElementSibling.classList.toggle("hidden");
        });
    });
});