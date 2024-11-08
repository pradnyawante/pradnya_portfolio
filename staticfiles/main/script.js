document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    form.addEventListener('submit', () => {
        alert('Thank you for submitting your name!'); // Alert on form submission
    });
});

document.querySelectorAll('nav a').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault(); // Prevent default anchor click behavior

        const target = document.querySelector(this.getAttribute('href')); // Get target section
        target.scrollIntoView({
            behavior: 'smooth' // Smooth scrolling effect
        });
    });
});