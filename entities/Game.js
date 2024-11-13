// Maintains the Game memory
class Game {
    constructor(ctx, p1, p2) {
        /** @type {CanvasRenderingContext2D} */
        this.ctx = ctx;
        this.players = [p1, p2];
    }

    // width and height of canvas
    updateSate(width, height, keyMaps) {
        /** @type {CanvasRenderingContext2D} */
        this.ctx.clearRect(0, 0, width, height);
        this.drawPlayerPositions(keyMaps);
    }

    drawPlayerPositions(keyMaps) {
        this.players.forEach(player => {
            this.ctx.fillStyle = player.color;
            this.getPlayerPositions(keyMaps)
            player.y = this.applyGravity(player.y)
            this.ctx.fillRect(player.x, player.y, player.width, player.height);
        });
    }

    getPlayerPositions(keyMaps) {
        const keys = Object.keys(keyMaps)
        console.log('THIS', keyMaps)
        keys.forEach((key) => { 
            if (typeof keyMaps[key] === 'function') {
                keyMaps[key](this.players[0]);
            }
        } )
    }

    applyGravity(y_pos) {
        var gravity = 10;
        return y_pos += gravity;
    }
    
}

export default Game;