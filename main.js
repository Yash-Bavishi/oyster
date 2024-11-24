import Game from "./entities/Game.js";
import Movable from "./entities/Movable.js";
import Player from "./entities/Player.js";
const canvas = document.getElementById('game');
const ctx = canvas.getContext('2d');

// for vscode to understand the type and provide autocomplete
/** @type {CanvasRenderingContext2D} */
var p1 = new Player('red', 80, 100, 70, 70, 2, 30);
var p2 = new Player('blue', 700, 100, 70, 70, 5, 3);

const game = new Game(ctx, p1, p2);
var map = {}

document.addEventListener('keydown', (e) => {
    switch (e.key) {
        case 'w':
            map[e.key] = Movable.jump;
            break;
        case 's':
            map[e.key] = Movable.moveDown;
            break;
        case 'd':
            map[e.key] = Movable.moveRight;
            break;
        case 'a':
            map[e.key] = Movable.moveLeft;
            break;
    }
})

let lastTime = 0;
const fps = 60;
const interval = 1000 / fps;

function gameLoop(timestamp) {
    if (timestamp - lastTime >= interval) {
        lastTime = timestamp;
        // Update and draw your game
        game.updateState(960, 540, map)
    }
    requestAnimationFrame(gameLoop);
}

window.onload = () => {
    // setInterval(() => game.updateSate(960, 540, map), 50)
    requestAnimationFrame(gameLoop);
}

document.addEventListener('keyup', (e) => {
    if (e.key) p1.canJump = true;
    delete map[e.key]
})

