document.addEventListener('DOMContentLoaded', function() {
    const hamburgerButton = document.getElementById('hamburgerButton');
    const mainNav = document.getElementById('mainNav');

    if (hamburgerButton && mainNav) {
        hamburgerButton.addEventListener('click', function() {
            // Alterna la clase 'is-active' en el menú de navegación
            mainNav.classList.toggle('is-active');

            // Alterna la clase 'is-active' en el botón de hamburguesa (para la animación de la X)
            this.classList.toggle('is-active'); // 'this' se refiere al hamburgerButton

            // Actualiza los atributos ARIA
            const isExpanded = mainNav.classList.contains('is-active');
            this.setAttribute('aria-expanded', isExpanded.toString());

            // Opcional: Cambiar el aria-label
            if (isExpanded) {
                this.setAttribute('aria-label', 'Cerrar menú de navegación');
            } else {
                this.setAttribute('aria-label', 'Abrir menú de navegación');
            }
        });

        // Opcional: Cerrar el menú si se hace clic fuera de él (en pantallas móviles)
        document.addEventListener('click', function(event) {
            // Solo ejecutar si el menú está visible (es decir, en modo hamburguesa)
            if (window.getComputedStyle(hamburgerButton).display === 'block') {
                const isClickInsideNav = mainNav.contains(event.target);
                const isClickOnHamburger = hamburgerButton.contains(event.target);

                if (mainNav.classList.contains('is-active') && !isClickInsideNav && !isClickOnHamburger) {
                    mainNav.classList.remove('is-active');
                    hamburgerButton.classList.remove('is-active');
                    hamburgerButton.setAttribute('aria-expanded', 'false');
                    hamburgerButton.setAttribute('aria-label', 'Abrir menú de navegación');
                }
            }
        });

    } else {
        // Esto es útil para depuración si algo no se encuentra
        if (!hamburgerButton) console.error("Botón de hamburguesa no encontrado. Revisa el ID 'hamburgerButton'.");
        if (!mainNav) console.error("Menú de navegación no encontrado. Revisa el ID 'mainNav'.");
    }
});