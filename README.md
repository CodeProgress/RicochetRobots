# RicochetRobots

![Reference Board](https://github.com/CodeProgress/RicochetRobots/blob/master/ricochet_robots_reference_board.jpg?raw=true)


# Robot Positions

  Each location on the board is represented by a (row, column) pair. This is to make indexing into the 2D array straightforward.
  Board state is maintained as a tuple of (row, column) pairs, one for each robot, e.g.
  
* ((red_row, red_column), (yellow_row, yellow_column), (green_row, green_column), (blue_row, blue_column))

# Quadrants

There are eight quadrants.
* QUAD_1A
* QUAD_2A
* QUAD_3A
* QUAD_4A
* QUAD_1B
* QUAD_2B
* QUAD_3B
* QUAD_4B

Each quadrant is a 8x8 section.

Four sections combine to make the board in the following manner:

|      top_left   | top_right|
| ------------- |-------------|
| bottom_left      | bottom_right |


The Reference Board is:

|      QUAD_4A   | QUAD_1B|
| ------------- |-------------|
| QUAD_2B      | QUAD_3A |


# Example solution

```python
board = BoardConfig.combine_quads_into_single_board(
    BoardConfig.QUAD_4A,
    BoardConfig.QUAD_1B,
    BoardConfig.QUAD_2B,
    BoardConfig.QUAD_3A)

rr = RRobots(board)

path = rr.breadth_first_search((2, 5), ((0, 0), (4, 7), (5, 12), (2, 1)))

print(path)

# [((0, 0), (4, 7), (5, 12), (2, 1)),
   ((0, 0), (4, 7), (5, 12), (2, 5))]

```

Explanation:
* The goal square (2, 5) corresponds to the blue hexagon
* Therefore the goal is to move the blue robot to square (2, 5)
* The blue robot starts on square (2, 1)
* The final path shows the blue robot moving 4 columns to the right from (2, 1) to (2, 5)

# Tools:

board_printer.py will print an ascii representation of a given configuration. Example: 
```
./board_printer.py 4a 1b 2b 3a 0,0 4,7 5,12 0,7
 ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
#  |  |  |  #  |  |  |  |  |  #  |  |  |  |  |  #
#R |  |  |  #  |  |  |B |  |  #  |  |  |  |  |  #
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
#  |  |  |  |  |  |  |  |  |  |  |  |  |GT#  |  #
#  |  |  |  |  |  |  |  |  |  |  |  |  |  #  |  #
 -- -- -- -- -- -- -- -- -- -- -- -- -- ## -- ##
#  |  |  |  |  |BH#  |  |  |  |  |  |  |  |  |  #
#  |  |  |  |  |  #  |  |  |  |  |  |  |  |  |  #
 -- -- -- -- -- ## -- -- -- ## -- -- -- -- -- --
#  |  |  |  |  |  |  |  |  #BQ|  |  |  |  |  |  #
#  |  |  |  |  |  |  |  |  #  |  |  |  |  |  |  #
 -- -- ## -- -- -- -- -- -- -- -- -- -- -- ## --
#  |  |GC#  |  |  |  |  |  |  |  |  |  |  |RC#  #
#  |  |  #  |  |  |  |Y |  |  |  |  |  |  |  #  #
 ## -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
#  |  |  |  |  |  |  #RT|  |  |  |  |  |  |  |  #
#  |  |  |  |  |  |  #  |  |  |  |  |G |  |  |  #
 -- ## -- -- -- -- -- ## -- -- -- -- -- -- -- --
#  #YQ|  |  |  |  |  |  |  |  |  |  #YH|  |  |  #
#  #  |  |  |  |  |  |  |  |  |  |  #  |  |  |  #
 -- -- -- -- -- -- -- ## ## -- -- -- ## -- -- --
#  |  |  |  |  |  |  #  |  #  |  |  |  |  |  |  #
#  |  |  |  |  |  |  #  |  #  |  |  |  |  |  |  #
 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
#  |  |  |  |  |  |  #  |  #  |  |  |  |  |  |  #
#  |  |  |  |  |  |  #  |  #  |  |  |  |  |  |  #
 -- -- -- -- -- -- -- ## ## -- -- -- -- -- -- --
#  |  |  |  #YT|  |  |  |  |  |  |  |  #BT|  |  #
#  |  |  |  #  |  |  |  |  |  |  |  |  #  |  |  #
 -- -- -- -- ## -- ## -- -- -- -- -- -- ## -- --
#  |  |  |  |  |  #BC|  |  |  |  |  |  |  |  |  #
#  |  |  |  |  |  #  |  |  |  |  |  |  |  |  |  #
 ## -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
#  |  |  |  |  |  |  |  |  |YC#  |  |  |  |  |  #
#  |  |  |  |  |  |  |  |  |  #  |  |  |  |  |  #
 -- -- -- -- -- -- -- -- -- ## -- -- -- -- -- ##
#  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  #
#  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  #
 -- ## -- -- -- -- -- -- -- -- -- -- -- -- ## --
#  |RH#  |  |  |  |  |  |  |  |  |  |  |  |RQ#  #
#  |  #  |  |  |  |  |  |  |  |  |  |  |  |  #  #
 -- -- -- -- -- -- -- -- -- -- ## -- -- -- -- --
#  |  |  |GQ#  |  |  |  |  |  #GH|  |  |  |  |  #
#  |  |  |  #  |  |  |  |  |  #  |  |  |  |  |  #
 -- -- -- ## -- -- -- -- -- -- -- -- -- -- -- --
#  |  |  |  |  #  |  |  |  |  |  |  #  |  |  |  #
#  |  |  |  |  #  |  |  |  |  |  |  #  |  |  |  #
 ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
```

board_solver.py will print a solution to a given configuration

Example:
```
$ ./board_solver.py 4a 1b 2b 3a 0,0 4,7 5,12 0,7 2,5
5 moves:
(0, 0), (0, 7), (5, 12), (0, 9)
(0, 0), (0, 4), (5, 12), (0, 9)
(0, 0), (0, 4), (5, 12), (0, 5)
(0, 0), (0, 4), (5, 12), (2, 5)
```

# Requirements:
* Python 3
* numpy

# Further Goals:

* Optimize algorithm further
* Convert board data to bitfields to help optimize lookup a little (16 bits should be sufficient)
* Create board/placement generators, which can generate non-trivial placements
* Create board/placement renderers for visualization
* Create training set for computer vision
  * High-quality images of the goal tiles, regular tiles, and boundaries
  * High-quality images of the robots to identify current locations (might be able to just use a histogram analysis if the tiling of the board is already known)
* Add support for silver robot
  * Ideally support an arbitrary number of robot/color combinations
* Add support for bumpers
