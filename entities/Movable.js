class Movable {

  static jump(p, ctx) {
    if (p.jumpsAvailable != 0) {
      if (p.jumpSize != 10) {
        p.y -= p.velocityY;
      }
      p.canJump = false
      p.jumpsAvailable--;
      p.jumpSize++;
    }
  }
  static moveDown(p) {
    p.y += p.velocityY;
  }

  static moveLeft(p) {
    p.x -= p.velocityX;
  }

  static moveRight(p) {
    p.x += p.velocityX;
  }

}

export default Movable