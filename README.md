## Description
This project is a 2D platformer game created using the Pygame library in Python. It includes features like a player character with animations, an enemy with a health system, and projectile shooting mechanics. The player can navigate, jump, and shoot bullets to defeat enemies, earning points while avoiding hits.

## Features
- **Player Controls**: Move left and right, jump, and shoot bullets.
- **Enemy Movement**: Enemies patrol between defined points.
- **Health System**: Enemies have health bars, and players lose points upon collision.
- **Sound Effects**: Background music, bullet firing, and hit effects.
- **Score Display**: A real-time score display on the screen.

## Installation
1. Install the required dependencies:
   ```bash
   pip install pygame
   ```

2. Run the game:
   ```bash
   python Tutorial_10.py
   ```

## Assets
- **Background**: `imgs/Backgrounds/bg.jpg`
- **Player Sprites**: `imgs/Character_1/`
- **Enemy Sprites**: `imgs/Character_2/`
- **Sounds**: `music/`
  - `bullet.mp3`: Bullet firing sound
  - `hit.mp3`: Enemy hit sound
  - `music.mp3`: Background music

## Controls
- **Arrow Keys**: Move left and right
- **Space**: Shoot bullets

## Game Logic
1. **Player Movement**: Controlled by arrow keys, with animations for left and right movement.
2. **Shooting Mechanism**: Bullets are fired in the direction the player is facing, with a limit of 5 bullets at a time.
3. **Enemy Behavior**: Enemies patrol between two points and decrease their health when hit by bullets.
4. **Collision Detection**: The player loses points upon collision with an enemy.
5. **Score System**: Score is displayed at the top right of the screen.

Credits: Tech With Tim <br>
Playlist: [Pygame Programming Tutorials](https://www.youtube.com/watch?v=i6xMBig-pP4&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5)

