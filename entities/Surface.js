// Surface class to create platforms and walls
class Surface {
	constructor(ctx, x, y, width, height, color) {
		this.ctx = ctx
		this.x = x;
		this.y = y;
		this.width = width;
		this.height = height;
		this.color = color;
	}

	// Method to draw the surface on the canvas
	draw() {
		this.ctx.fillStyle = this.color;
		this.ctx.fillRect(this.x, this.y, this.width, this.height);
	}

	// Optional: Method to check if a point is within the surface's bounds
	contains(x, y, width, height) {
		// return x >= this.x 
		// && x <= this.x + this.width 
		// && y >= this.y 
		// && y <= this.y + this.height;
		return (x + width > this.x && x < this.x + this.width) && (y + height > this.y && y + height <= this.y + this.height)
	}

	hasHitSide(x, y, width, height) {
		// return x >= this.x 
		// && x <= this.x + this.width 
		// && y >= this.y 
		// && y <= this.y + this.height;

		//console.log(x, this.x + this.width);
		

		return (x > this.x 
			&& x < this.x + this.width
			&& x + width >= this.x

		)
	}

	isOnRight(x, y, width, height) {
		// The player's right side should be greater than the surface's left edge
		// and the player's left side should still be inside the surface horizontally
		
		return (x + width > this.x && x + width <= this.x + (this.width/2)) && (y + height > this.y && y < this.y + this.height);
	}

	// Checks if the left side of the object is touching the surface
	isOnLeft(x, y, width, height) {
		// The player's left side should be less than the surface's right edge
		// and the player's right side should still be inside the surface horizontally
		//return (x < this.x + this.width && x + width >= this.x) &&
		//	(y + height > this.y && y < this.y + this.height);
		return (x < this.x + this.width && x >= this.x + (this.width / 2)) && (y + height > this.y && y < this.y + this.height);

	}
}

export default Surface