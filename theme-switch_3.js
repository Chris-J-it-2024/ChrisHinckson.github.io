// Theme switching functionality
document.addEventListener('DOMContentLoaded', function() {
    const themeToggle = document.getElementById('themeToggle');
    const matrixStyle = document.getElementById('matrix-style');
    const normalStyle = document.getElementById('normal-style');
    
    // Check saved theme preference
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'normal') {
        enableNormalTheme();
        themeToggle.checked = true;
    }

    // Theme toggle handler
    themeToggle.addEventListener('change', function() {
        if (this.checked) {
            enableNormalTheme();
            localStorage.setItem('theme', 'normal');
        } else {
            enableMatrixTheme();
            localStorage.setItem('theme', 'matrix');
        }
    });

    function enableNormalTheme() {
        matrixStyle.disabled = true;
        normalStyle.disabled = false;
        // Stop matrix rain animation if it's running
        if (window.stopMatrixRain) {
            window.stopMatrixRain();
        }
    }

    function enableMatrixTheme() {
        matrixStyle.disabled = false;
        normalStyle.disabled = true;
        // Restart matrix rain animation
        if (window.startMatrixRain) {
            window.startMatrixRain();
        }
    }
});