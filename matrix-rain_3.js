// Matrix Rain Animation Script for theme-enabled pages
class MatrixRain {
    constructor() {
        this.canvas = document.getElementById('matrix_rain');
        this.ctx = this.canvas.getContext('2d');

        // Animation control
        this.is_running = true;
        this.animation_id = null;

        // Characters for the rain effect
        this.matrix_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789@#$%^&*()*&^%".split("");

        // Rain configuration
        this.font_size = 20; // Increased font size
        this.drops = [];

        // Setup
        this.setup_canvas();
        this.initialize_drops();
        this.setup_event_listeners();
    }

    setup_canvas() {
        this.resize_canvas();
    }

    setup_event_listeners() {
        window.addEventListener('resize', () => this.resize_canvas());
    }

    resize_canvas() {
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
        this.initialize_drops();
    }

    initialize_drops() {
        const columns = Math.floor(this.canvas.width / this.font_size);
        this.drops = Array(columns).fill(1);
    }

    draw() {
        this.ctx.fillStyle = 'rgba(0, 0, 0, 0.1)'; // Increased fade opacity
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        this.ctx.fillStyle = '#0F0';
        this.ctx.font = this.font_size + 'px monospace';

        this.drops.forEach((drop, i) => {
            const char = this.matrix_chars[Math.floor(Math.random() * this.matrix_chars.length)];

            const x = i * this.font_size;
            const y = drop * this.font_size;
            this.ctx.fillText(char, x, y);

            if (y > this.canvas.height && Math.random() > 0.975) {
                this.drops[i] = 0;
            } else {
                this.drops[i] += 0.5; // Increased drop speed
            }
        });
    }

    animate() {
        if (!this.is_running) return;

        this.draw();
        this.animation_id = requestAnimationFrame(() => this.animate());
    }

    start() {
        if (!this.is_running) {
            this.is_running = true;
            this.animate();
        }
    }

    stop() {
        this.is_running = false;
        if (this.animation_id) {
            cancelAnimationFrame(this.animation_id);
            this.animation_id = null;
        }
    }
}

const matrix_rain = new MatrixRain();

window.stop_matrix_rain = () => matrix_rain.stop();
window.start_matrix_rain = () => matrix_rain.start();

matrix_rain.animate();
