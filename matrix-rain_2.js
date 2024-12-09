// Matrix Rain Animation Script for theme-enabled pages
class MatrixRain {
    constructor() {
        // Initialize canvas
        this.canvas = document.getElementById('matrix-rain');
        this.ctx = this.canvas.getContext('2d');
        
        // Animation control
        this.isRunning = true;
        this.animationId = null;
        
        // Characters for the rain effect
        this.matrixChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789@#$%^&*()*&^%".split("");
        
        // Rain configuration
        this.fontSize = 16;
        this.drops = [];
        
        // Setup
        this.setupCanvas();
        this.initializeDrops();
        this.setupEventListeners();
    }

    setupCanvas() {
        // Set initial canvas size
        this.resizeCanvas();
    }

    setupEventListeners() {
        // Handle window resize
        window.addEventListener('resize', () => this.resizeCanvas());
    }

    resizeCanvas() {
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
        // Reinitialize drops after resize
        this.initializeDrops();
    }

    initializeDrops() {
        const columns = Math.floor(this.canvas.width / this.fontSize);
        this.drops = Array(columns).fill(1);
    }

    draw() {
        // Create fade effect
        this.ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        // Set text properties
        this.ctx.fillStyle = '#0F0';
        this.ctx.font = this.fontSize + 'px monospace';

        // Draw rain drops
        this.drops.forEach((drop, i) => {
            // Get random character
            const char = this.matrixChars[Math.floor(Math.random() * this.matrixChars.length)];
            
            // Draw the character
            const x = i * this.fontSize;
            const y = drop * this.fontSize;
            this.ctx.fillText(char, x, y);

            // Reset drop or move it down
            if (y > this.canvas.height && Math.random() > 0.975) {
                this.drops[i] = 0;
            } else {
                this.drops[i]++;
            }
        });
    }

    animate() {
        if (!this.isRunning) return;
        
        this.draw();
        this.animationId = requestAnimationFrame(() => this.animate());
    }

    start() {
        if (!this.isRunning) {
            this.isRunning = true;
            this.animate();
        }
    }

    stop() {
        this.isRunning = false;
        if (this.animationId) {
            cancelAnimationFrame(this.animationId);
            this.animationId = null;
        }
    }
}

// Initialize and expose control functions
const matrixRain = new MatrixRain();

// Global control functions for theme switcher
window.stopMatrixRain = () => matrixRain.stop();
window.startMatrixRain = () => matrixRain.start();

// Start animation
matrixRain.animate();