document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.querySelector('.menu_toggle');
    const sidebar = document.querySelector('.sidebar');

    menuToggle.addEventListener('click', function() {
        sidebar.classList.toggle('open');
    });
});
