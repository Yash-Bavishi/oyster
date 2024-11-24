# Notes

## Purpose of the game 
I want this game to be a bond between a family between `father` and `son`, 2 friends who hit nostalgia when talking about this game. My father and elder brother introduced me to computer I remember playing GTA vice city, Pooh and vinnie, contra 4 and so many games with them. I learned about computers from game and I want the same with `Oyster`. 

- Yash:
    - `Game` will maintain the state of the game. only game can call update state

## Gravity 

- All the classes where gravity is applicable decrease their 'Y' positions indefinetely
- I am chosing gravity not to be a class since its a constant and there are no methods to it
- Gravity is constant which is `9.8 m/s^2` 
- The speed at which object fall is based upon air resistance and weight in future all objects will have weights (if needed)
- **FOR NOW LETS ASSUME THAT WE ARE FIGHTING IN SPACE**

## Movement

- Game will continously check for keyboard strokes.
  - It will be a `dictionary` with key being the stroke and value being the function


### Jump 

```math
jump = (force x weight) / (mass x gravity)
```

- Current jump logic is actually wrong because canvas will redraw the shape at that positions rather than actual jumping and making player jump

#### Jump algorthm

PROBLEM 1 :- determine the 'w' is pressed (done)
PROBLEM 2 :- For 100ms increase player position by 2px till player positions doesn't hit 10px (for now) 
  - if it hits 10px stop going up
  - so till timer doesn't hit 500ms the player will keep going up (implement this)