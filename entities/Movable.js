class Movable {

  static jump(p, ctx) {
    const destPosition = p.y - 150;
    if (p.jumpsAvailable != 0) {
      while (p.y >= destPosition) {
        p.y -= p.velocityY;
        ctx.fillRect(p.x, p.y, p.width, p.height);
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