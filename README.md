﻿# SlidingPuzzle - OOP Structure

## MODE
- `Human-Mode`
- `Solver` using some Algorithms in AI such as:
    - BFS
    - DFS
    - A* using manhattan heuristic
## Demo
- `Human-Mode`
</br>

![](https://github.com/Minnass/SlidingPuzzle-SearchingAlgorithms/blob/main/image/ezgif.com-gif-to-webp.gif)
- `Solver`
</br>

![](https://github.com/Minnass/SlidingPuzzle-SearchingAlgorithms/blob/main/image/ezgif.com-video-to-gif.gif)
## Setting up

- Folder Structure
```
SliddingPuzzlePygame
    ├── .vscode
    │   ├── launch.json
    |     
    ├── image
    │   
    |   
    ├── source
    |         ├── GameSettings
    |         |              ├──Board.py
    |         |              ├──settings.py
    |         |              ├──Tile.py
    |         |              ├──UIElement.py
    |         |              ├──util.py
    |         |
    |         └── solver
    |                   ├──__init__.py
    |                   ├──Algorithm.py
    |                   ├──AStar.py
    |                   ├──BFS.py
    |                   ├──DFS.py
    |                   ├──HumanResolver.py
    ├── main.py
       
```
To tackle the puzzles on your own computer, you'll need a Python  environment with the dependencies (pygame) installed.

One way to do this is as follows.

1. Check you have Python  installed by printing the version of Python:
```
python -V
    if not installed 
sudo apt-get install python
```
2. Check you have Pygame installed or not by checking
```
pip show pygame 
    if not installed:
pip install pygame
```
2. Clone the puzzle repository using Git:

```
git clonehttps://github.com/Minnass/SlidingPuzzle-SearchingAlgorithms.git
```

3. Move into subfolder `./source` then using command on terminal as following:
```
python ./main.py
```
