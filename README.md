# Ant and the Grasshopper
In this game, you will control a grasshopper as it walks to the nest, hops over ants, picks up the food inside the nest, and drops it at home
## Gameplay
When the game starts, it shows the following "picture" and prompts the player to enter a command.
```
$python3 AntAndTheGrassHopper.py
[] G . . . a . . a . a . [***]
>
```
## Terminology for the symbols
[]- The Grasshopper's home. It is empty at first, because the Grasshopper doesn't have any food.
G - The Grasshopper, which is controlled by the player."
. - an empty space. The Grasshopper can walk or hop onto empty spaces.
a - an Ant. All ants are stationary. The Grasshopper should hop over Ants.
[***]- the Ants' nest. Each * is a bit of food, which the Grasshopper can pick up.

## Commands
The player can instruct the grasshopper to perform each of these actions. After each action is performed, the game updates the picture and shows it to the user.
All commands are case-insensitive. If an invalid command is entered, the game prints Invalid command and prompts the player to enter another command.
```
$ python grasshopper.py
[] G . . . a . . a . a . [***] > spam
Invalid command
>
```
### Walk L
The Grasshopper moves one space to the left.
'''
[] . . G . a . . a . a . [***] 
> WALK L
[] . G . . a . . a . a . [***] 
>
'''
If the Grasshopper is already next to its home, this command has no effect.
```
[] G . . . a . . a . a . [***] 
> WALK L
[] G . . . a . . a . a . [***] 
>
```
If the Grasshopper moves onto an Ant, the Grasshopper will be attacked and the game will end.
```
[] . . . . a G . a . a . [***]
> WALK L
Arrgh!! An Ant attacked you. Game over.
```
### Walk R
The same as WALK L , but the Grasshopper moves to the right instead. Like before, this command has no
effect if the Grasshopper is already next to the Ants' nest.
### Hop L
The Grasshopper moves to the left, jumping over one spot and landing on the next.
```
[] . . G . a . . a . a . [***] > HOP L
[] G . . . a . . a . a . [***] >
```
```
[] . . . . a G . a . a . [***] > HOP L
[] . . . G a . . a . a . [***] >
```
Like WALK L , this command has no effect if the Grasshopper is already next to its home.
If hopping left results in the Grasshopper landing on top of its home, the HOP L command will instead produce the same effect as WALK L .
```
[] . G . . a . . a . a . [***] > HOP L
[] G . . . a . . a . a . [***] >
```
If the Grasshopper hops onto an Ant, the Grasshopper will be attacked and the game will end.
```
[] . . . . a . G a . a . [***]
> HOP L
Arrgh!! An Ant attacked you. Game over.
```
### Hop R
The same as HOP L , but the Grasshopper moves to the right instead. Like before, the Grasshopper cannot
hop over or onto the Ants' nest.

### Pick Up
The Grasshopper picks up a bit of food from the Ants' nest, which it can carry back to its own home.

```
[] . . . . a . . a . a G [***] > PICK UP
[] . . . . a . . a . a G* [**] >
```
This command is valid only when:
- The Grasshopper is next to the Ants' nest, 
- the Ants' nest contains food, and
- The Grasshopper isn't already holding food.
If these conditions aren't true, the game prints Cannot pick up food and prompts the player to enter another command.
```
[] G . . . a . . a . a . [***] > PICK UP
Cannot pick up food
>
```
### Drop
The Grasshopper drops the bit of food it was carrying.
```
[] G* . . . a . . a . a . [**] 
> PICK UP
[*] G . . . a . . a . a . [**] 
>
```

```
[*] G* . . . a . . a . a . [*] > PICK UP
[**] G . . . a . . a . a . [*] >
```
This command is valid only when:
- The Grasshopper is next to its own home, and
- The Grasshopper is already holding food.
If these conditions aren't true, the game prints Cannot drop food and prompts the player to enter another command.
```
[] G . . . a . . a . a . [***] > DROP
Cannot drop food
>
```

When the last bit of food is dropped, the Grasshopper will have succeeded and the game will end.
```
[**] G* . . . a . . a . a . [**]
> DROP
[***] G . . . a . . a . a . [**]
Congratulations Grasshopper, you now have enough food to last the winter!
```
### Quit
At any point, the player may choose to end the game.
```
[] . . . . a . . a . a G* [**] > QUIT
Goodbye Grasshopper!
```
## Technologies Used
- Python 3
- Atom

## Launch
The project can be run on an IDE using python3. You can first open a command prompt window and go to the directory where you saved the java program. Type 'python3 AntAndTheGrassHopper.py' and press enter to compile and run your code
## Setup
To set up the program. Type this into the command terminal:

```
$python3 AntAndTheGrassHopper.py
```

