# Ant and the Grasshopper
In this game, you will control a grasshopper as it walks to the nest, hops over ants, picks up the food inside the nest, and drops it at home
## Gameplay
When the game starts, it shows the following "picture" and prompts the player to enter a command.
```
$python grasshopper.py
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
