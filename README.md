# 11-Puzzle
11-Puzzle Problem AI solver for CS-UY 4613

By Kevin Lee (KL3642)

This program uses Weighted A* Search to search for the optimal set of 
moves to achieve the goal state from the given initial state.

### How to use
1. Open shell or terminal in project dir (C:\\...\\11-Puzzle).
2. Use the following syntax:
   1. `python3 puzzle.py 'text_file.txt' 'w'`
      1. Note: All files used must be present in project dir including input files.
   2. For example: `python3 puzzle.py Input1.txt 1.2`
3. The program will create an `output.txt` file in the same directory
   1. Note: Repeated usage of the program will continually append to the file `output.txt`
   2. If you wish to run the program multiple times, you must either rename `output.txt`
   or delete it.

### Future Work
- Redesign structure of code base to be more modular and general
  - Instead of coding Manhattan Distance Heuristic into the main code, 
  abstract by creating a Heuristic class with different heuristics inheriting from
  the main class
  - Create Problem class with the same principles as Heuristic, where different
  versions of sliding puzzles can be solved (8-Puzzle, 15-Puzzle, etc.)
  - This will require changing various functions of code including input parsing