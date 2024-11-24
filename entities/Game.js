import Surface from "./Surface.js";


// Maintains the Game memory
class Game {
    constructor(ctx, p1, p2) {
        /** @type {CanvasRenderingContext2D} */
        this.ctx = ctx;
        this.players = [p1, p2];

        // Example surfaces (platforms and walls)
        this.surfaces = [
            new Surface(this.ctx, 100, 400, 700, 20, "cyan"),  // Platform
        ];
        this.playerCollided = 0;
    }

    // width and height of canvas
    updateState(width, height, keyMaps) {
        console.log("GOD");
        /** @type {CanvasRenderingContext2D} */
        this.ctx.clearRect(0, 0, width, height);
        this.drawPlayerPositions(keyMaps);
        // Draw each surface (platform/wall)
        this.surfaces.forEach(surface => surface.draw(this.ctx));
        this.getPlayerCollisions();
    }

    drawPlayerPositions(keyMaps) {
        this.players.forEach(player => {
            this.ctx.fillStyle = player.color;
            this.getPlayerPositions(keyMaps)
            player.y = this.applyGravity(player.y)

            // Checking if the player is going outside canvas
            if (player.y <= 0) {
                player.y = 0;
            };

            if (player.y + player.height >= this.ctx.canvas.height) {
                player.y = this.ctx.canvas.height - player.height;
            };

            if (player.x <= 0) {
                player.x = 0;
            }

            if (player.x + player.width >= this.ctx.canvas.width) {
                player.x = this.ctx.canvas.width - player.width;
            }

            for (let surface of this.surfaces) {
                // Check if the player is standing on a platform (a rectangle)
                if (surface.contains(player.x, player.y, player.width, player.height) && (surface.y - player.height) >= 0) {
                    player.y = surface.y - player.height
                    player.jumpsAvailable = 3;
                }
                if (surface.isOnLeft(player.x, player.y, player.width, player.height)) {
                    player.x = surface.x + surface.width
                }
                if (surface.isOnRight(player.x, player.y, player.width, player.height)) {
                    player.x = surface.x - player.width
                }
                if (surface.hasHitSide(player.x, player.y, player.width, player.height)) {
                    player.jumpsAvailable = 3;
                }
            }
            this.ctx.fillRect(player.x, player.y, player.width, player.height);
        });
    }

    getPlayerPositions(keyMaps) {
        const keys = Object.keys(keyMaps)
        keys.forEach((key) => {
            if (typeof keyMaps[key] === 'function') {
                if (this.players[0].canJump) {
                    keyMaps[key](this.players[0], this.ctx);
                }
            }
        })
    }

    getPlayerCollisions() {
        var p1 = this.players[0];
        var p2 = this.players[1];
        // Horizontal Collision
        if (p1.x >= (p2.x - p2.width) && p2.x >= (p1.x - p1.width) && p1.y <= p2.y && p1.y >= (p2.y - p2.height) || (p1.y - p1.height > p2.y - p2.height) && p1.y - p1.height < p2.y){
            console.log("Colliison Found")
        }

        // Vertical Collision
        // if () {
        //     console.log("vertical collision");
        // }

    }

    applyGravity(y_pos) {
        var gravity = 10;
        return y_pos += gravity;
    }

}

export default Game;