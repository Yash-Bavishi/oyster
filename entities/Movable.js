class Movable {

  static moveUp(p) {
    console.log("hi", p.canJump, p.jumpsAvailable);
      if (p.canJump) {
      switch (p.jumpsAvailable) {
        case 3:
          p.y -= 200;
          p.jumpsAvailable = p.jumpsAvailable - 1;
          break;
        case 2:
          p.y -= 210;
          p.jumpsAvailable = p.jumpsAvailable - 1;
          break;
        case 1:
          p.y -= 250;
          p.jumpsAvailable = p.jumpsAvailable - 1;
          break;
      }
      p.canJump = false;
    }
  }

  static moveDown(p) {
    p.y += 10;
  }

  static moveLeft(p) {
    p.x -= 10;
  }

  static moveRight(p) {
    p.x += 10;
  }


}

export default Movable