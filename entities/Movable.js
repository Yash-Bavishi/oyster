class Movable {

  static jump(p) {
    const destPosition = p.y - 150;
    if (p.jumpsAvailable != 0) {
      while (p.y >= destPosition) {
        p.y -= p.velocityY;
      }
      p.canJump = false
      p.jumpsAvailable--;
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