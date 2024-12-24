Group project for final for CS110

# Mars Patrol
## CS110 Final Project  Fall, 2023

## Team Members

Steven Lin

Andrew Zou

***

## Project Description

A version  of Moon Patrol. 

***    

## GUI Design

### Initial Design

![<Screenshot 2023-11-13 at 5.57.43 PM.png>](assets/gui.jpg)

### Final Design

![assets/finalgui.jpg](<assets/Screenshot 2023-12-08 at 2.33.39 PM.png>)

## Program Design

### Features

1. start menu
2. moveable character
3. obstacle collisions
4. scrolling background
5. game over screen

### Data Permanence Feature 
High score

### Classes

Background: creates a scrolling background (screen, width, height, x)  
- init: creates the background
- update: updates the background every frame
- draw: draws the updated background  

Controller: The controller (no parameters)
- init: creates the values for the controller
- mainlooop: determines the states of the game
- menuloop: the menu screen
- gameloop: the main game
- gameoverloop: the game over screen  

Player: creates the player sprite (pygame.sprite.Sprite)
- init: creates the player dinosaur
- run: the running animation
- jump: the jumping animation
- duck: the ducking animation
- stand: the standing animation
- update: updates the player 
- draw: draws the new updated player  

Obstacles: The main obstacles
- init: creates the obstacles
- update: updates the location of obstacles
- obstacle_select: selects between Asteroid and Radar classes
- draw: draws the updated obstacle  

Asteroid: The asteroid obstacle
- init: creates the asteroid obstacles
- update: updates the asteroid obstacle location
- draw: draws the updated asteroid

Radar: The radar obstacle
- init: creates the radar obstacle
- update: updates the radar obstacle location
- draw: draws the updated radar

Score: Creates the score counter
- init: creates a score
- str: returns the score as a string
- update: updates the current score
- save_high: saves the high score
- open_high: opens the previous high score

Highscore: Keeps track of high score
- init: passed
- save_high: saves the high score
- open_high: opens the previous high score

## ATP

Test Case 1: Player Movement

Test Description: Verify that the player jumps/ducks as expected
Test Steps:
Start the game.
Press the spacebar or up arrow.
Verify the player jumps upwards and then lands back down.
Press the down arrow.
Verify the player ducks
Expected Outcome: The player should jump up and down or ducks in response to the spacebar or arrow keys.

Test Case 2: Collision Detection and Game Over condition

Test Description: Ensure that collisions between the player and obstacles are detected correctly.
Test Steps:
Start the game.
Play until player touches obstacle. 
Verify the collison is detected and game ends with game over screen.
Expected Outcome: When player touches obstacles, the game should end with game over screen.

Test Case 3: Error Handling

Test Description: Verify that the program handles unexpected inputs gracefully.
Test Steps:
Start the game.
Enter invalid characters or inputs during gameplay.
Verify that the program does not crash and displays appropriate error messages.

Test Case 4: Score

Test Description: The score should be tracked as the game progresses 
Test Steps:
Start the game.
Play game.
Observe the score counter go up.
Lose the game.
Verify score counter ends.

Expected Outcome: Score counter should go up when game is being played and stop when the game is over.

Test Case 5: Play again

Test Description:  Verify the game will restart after game over screen
Test Steps: 
Start the game.
Play until game over screen.
Press play again.
Verify the game starts again with new score.
Expected Outcome: Score resets and game begins again

