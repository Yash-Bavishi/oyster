import Movable from "./Movable.js";

class Player extends Movable {
    constructor(color, x, y, height, width) {
        super();
        this.x = x;
        this.y = y;
        this.height = height;
        this.width = width;
        this.color = color;
    }
}


export default Player;