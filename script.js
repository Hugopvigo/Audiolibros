document.addEventListener('DOMContentLoaded', () => {
    // 1. Audio Visualizer Animation
    const bars = document.querySelectorAll('.bar');
    
    function animateVisualizer() {
        bars.forEach(bar => {
            const height = Math.random() * (60 - 10) + 10;
            bar.style.height = `${height}px`;
        });
    }

    // Actualizar visualizador cada 150ms
    setInterval(animateVisualizer, 150);

    // 2. Mouse Parallax for Blobs
    const blobs = document.querySelectorAll('.blob');
    
    document.addEventListener('mousemove', (e) => {
        const { clientX, clientY } = e;
        const centerX = window.innerWidth / 2;
        const centerY = window.innerHeight / 2;
        
        const moveX = (clientX - centerX) / 50;
        const moveY = (clientY - centerY) / 50;

        blobs.forEach((blob, index) => {
            const speed = (index + 1) * 0.5;
            blob.style.transform = `translate(${moveX * speed}px, ${moveY * speed}px)`;
        });
    });

    // 3. Smooth Hover for Buttons
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(btn => {
        btn.addEventListener('mouseenter', () => {
            btn.style.transform = 'translateY(-3px) scale(1.02)';
        });
        btn.addEventListener('mouseleave', () => {
            btn.style.transform = 'translateY(0) scale(1)';
        });
    });
});
