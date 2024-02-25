document.addEventListener("DOMContentLoaded", function () {

    const menuIcon = document.getElementById("menu-icon");
    const LinkDisp = document.querySelector(".index_header");
    const menuClose = document.querySelector(".menu-close");
    const menuBtn = document.querySelector(".menu-btn");
    const overlay = document.getElementById('overlay');
    const body = document.body;

    menuIcon.addEventListener("click", () => {
        if (LinkDisp.style.display === "none" || LinkDisp.style.display === "") {
            LinkDisp.style.display = "flex";
            LinkDisp.classList.add("open");
            menuClose.style.display = "block";
            body.style.overflow = "hidden";
            overlay.style.display = 'block';

            // Apply the opening animation
            // LinkDisp.style.animation = "openMenu 0.5s";
        } else {
            LinkDisp.classList.add("close"); // Add the 'close' class

            // Apply the closing animation
            // LinkDisp.style.animation = "closeMenu 0.5s";

            // Add a delay to allow the closing animation to complete before removing the class
            setTimeout(() => {
                LinkDisp.classList.remove("open", "close"); // Remove both 'open' and 'close' classes
                LinkDisp.style.display = "none";
                menuClose.style.display = "none";
                body.style.overflow = "auto";
                overlay.style.display = 'none';
                LinkDisp.style.animation = "none";
            }, 500); // Adjust the delay to match the animation duration (0.5s in this case)
        }
    });

    menuClose.addEventListener("click", () => {
        LinkDisp.classList.add("close"); // Add the 'close' class

        // Apply the closing animation
        // LinkDisp.style.animation = "closeMenu 0.5s";

        // Add a delay to allow the closing animation to complete before removing the class
        setTimeout(() => {
            LinkDisp.classList.remove("open", "close"); // Remove both 'open' and 'close' classes
            LinkDisp.style.display = "none";
            menuClose.style.display = "none";
            body.style.overflow = "auto";
            overlay.style.display = 'none';
            LinkDisp.style.animation = "none";
        }, 500); // Adjust the delay to match the animation duration (0.5s in this case)
    });
});
