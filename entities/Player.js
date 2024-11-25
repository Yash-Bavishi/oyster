import Movable from "./Movable.js";

class Player extends Movable {
    constructor(color, x, y, height, width, velocityX, velocityY) {
        super();
        this.x = x;
        this.y = y;
        this.height = height;
        this.width = width;
        this.color = color;
        this.jumpsAvailable = 3;
        this.canJump = true;
        this.velocityX = velocityX;
        this.velocityY = velocityY;
        this.jumpSize = 0;
    }
}


export default Player;