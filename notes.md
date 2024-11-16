# Notes

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

- Player needs to jumps 3 times max 
  - 1st jump 10px
  - 2nd jump 5px
  - 3rd Jump 2px