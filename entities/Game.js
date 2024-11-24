import Surface from "./Surface.js";


// Maintains the Game memory
class Game {
    constructor(ctx, p1, p2) {
        /** @type {CanvasRenderingContext2D} */
        this.ctx = ctx;
        this.players = [p1, p2];

        // Example surfaces (platforms and walls)
        this.surfaces = [
            new Surface(this.ctx, 100, 500, 200, 20, "green"), // Platform
            new Surface(this.ctx, 400, 400, 50, 20, "blue"),  // Platform
            new Surface(this.ctx, 0, 550, this.ctx.canvas.width, 50, "brown"), // Bottom wall
            //new Surface(this.ctx, 0, 0, 50, this.ctx.canvas.height, "brown"), // Left wall
            new Surface(this.ctx, 900, 0, 50, this.ctx.canvas.height, "brown") // Right wall
        ];
    }

    // width and height of canvas
    updateState(width, height, keyMaps) {
        /** @type {CanvasRenderingContext2D} */
        this.ctx.clearRect(0, 0, width, height);
        this.drawPlayerPositions(keyMaps);

        // Draw each surface (platform/wall)
        this.surfaces.forEach(surface => surface.draw(this.ctx));
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
                    //console.log('hit side')
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
                    keyMaps[key](this.players[0]);
                }
            }
        })
    }

    applyGravity(y_pos) {
        var gravity = 10;
        return y_pos += gravity;
    }

}

export default Game;