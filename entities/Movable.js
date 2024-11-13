class Movable {

   static moveUp(p) {
    p.y -= 20;
   }

  static moveDown(p)  {
    p.y += 10;
   } 

  static moveLeft(p)  {
    p.x -= 10;
   } 

  static moveRight(p)  {
    p.x += 10;
   } 


}

export default Movable