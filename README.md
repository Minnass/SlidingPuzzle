# SlidingPuzzle - OOP 

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
1. Clone repo ```git@github.com:imshubhamsingh/15-puzzle.git```
2. 
## Folder Structure
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
To tackle the puzzles on your own computer, you'll need a Python 3 environment with the dependencies (namely pandas) installed.

One way to do this is as follows. I'm using a bash shell, the procedure with Mac OS should be essentially the same. Windows, I'm not sure about.

1. Check you have Python 3 installed by printing the version of Python:
```
python -V
```

2. Clone the puzzle repository using Git:

```
git clone https://github.com/ajcr/100-pandas-puzzles.git
```

3. Install the dependencies (**caution**: if you don't want to modify any Python modules in your active environment, consider using a virtual environment instead):

```
python -m pip install -r requirements.txt
```

4. Launch a jupyter notebook server:

```