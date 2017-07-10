import numpy

# Directions
NORTH = 'N'
EAST = 'E'
SOUTH = 'S'
WEST = 'W'

DIRECTIONS = (NORTH, EAST, SOUTH, WEST)

# Colors
RED = 'R'
YELLOW = 'Y'
GREEN = 'G'
BLUE = 'B'

COLORS = (RED, YELLOW, GREEN, BLUE)

# Shapes
CIRCLE = 'C'
TRIANGLE = 'T'
SQUARE = 'Q'
HEXAGON = 'H'

SHAPES = (CIRCLE, TRIANGLE, SQUARE, HEXAGON)

rotated_wall_transformations = {
    NORTH: EAST,
    EAST: SOUTH,
    SOUTH: WEST,
    WEST: NORTH,
}


def compile_board(board):
    return numpy.array(board).reshape((8, 8))

# Boards adapted from https://github.com/fogleman/Ricochet/blob/master/model.py

# Quads
# TODO: it might be a little nicer to identify them by their color code
QUAD_1A = compile_board(
    ['NW', 'N', 'N', 'N', 'NE', 'NW', 'N', 'N',
           'W', 'S', 'X', 'X', 'X', 'X', 'SEYH', 'W',
           'WE', 'NWGT', 'X', 'X', 'X', 'X', 'N', 'X',
           'W', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
           'W',  'X', 'X', 'X', 'X', 'X', 'S', 'X',
           'SW', 'X', 'X', 'X', 'X', 'X', 'NEBQ', 'W',
           'NW', 'X', 'E', 'SWRC', 'X', 'X', 'X', 'S',
           'W', 'X',  'X', 'N', 'X', 'X', 'E', 'NW'
     ])

QUAD_2A = compile_board(
    ['NW', 'N', 'N', 'NE', 'NW', 'N', 'N', 'N',
           'W', 'X', 'X', 'X', 'X', 'E', 'SWBC', 'X',
           'W', 'S', 'X', 'X', 'X', 'X', 'N', 'X',
           'W', 'NEYT', 'W', 'X', 'X', 'S', 'X', 'X',
           'W', 'X', 'X', 'X', 'E', 'NWGQ', 'X', 'X',
           'W', 'X', 'SERH', 'W', 'X', 'X', 'X', 'X',
           'SW', 'X', 'N', 'X', 'X', 'X', 'X', 'S',
           'NW', 'X', 'X', 'X', 'X', 'X', 'E', 'NW'
     ])

QUAD_3A = compile_board(
    ['NW', 'N', 'N', 'NE', 'NW', 'N', 'N', 'N',
           'W', 'X', 'X', 'X', 'X', 'SEGH', 'W', 'X',
           'WE', 'SWRQ', 'X', 'X', 'X', 'N', 'X', 'X',
           'SW', 'N', 'X', 'X', 'X', 'X', 'S', 'X',
           'NW', 'X', 'X', 'X', 'X', 'E', 'NWYC', 'X',
           'W', 'X', 'S', 'X', 'X', 'X', 'X', 'X',
           'W', 'X', 'NEBT', 'W', 'X', 'X', 'X', 'S',
           'W', 'X', 'X', 'X', 'X', 'X', 'E', 'NW'
     ])

QUAD_4A = compile_board(
    ['NW', 'N', 'N', 'NE', 'NW', 'N', 'N', 'N',
           'W', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
           'W', 'X', 'X', 'X', 'X', 'SEBH', 'W', 'X',
           'W', 'X', 'S', 'X', 'X', 'N', 'X', 'X',
           'SW', 'X', 'NEGC', 'W', 'X', 'X', 'X', 'X',
           'NW', 'S', 'X', 'X', 'X', 'X', 'E', 'SWRT',
           'WE', 'NWYQ', 'X', 'X', 'X', 'X', 'X', 'NS',
           'W', 'X', 'X', 'X', 'X', 'X', 'E', 'NW'
     ])

QUAD_1B = compile_board(
    ['NW', 'NE', 'NW', 'N', 'NS', 'N', 'N', 'N',
           'W', 'S', 'X', 'E', 'NWRC', 'X', 'X', 'X',
           'W', 'NEGT', 'W', 'X', 'X', 'X', 'X', 'X',
           'W', 'X', 'X', 'X', 'X', 'X', 'SEYH', 'W',
           'W', 'X', 'X', 'X', 'X', 'X', 'N', 'X',
           'SW', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
           'NW', 'X', 'E', 'SWBQ', 'X', 'X', 'X', 'S',
           'W', 'X', 'X', 'N', 'X', 'X', 'E', 'NW'
     ])

QUAD_2B = compile_board(
    ['NW', 'N', 'N', 'N', 'NE', 'NW', 'N', 'N',
           'W', 'X', 'SERH', 'W', 'X', 'X', 'X', 'X',
           'W', 'X', 'N', 'X', 'X', 'X', 'X', 'X',
           'WE', 'SWGQ', 'X', 'X', 'X', 'X', 'S', 'X',
           'SW', 'N', 'X', 'X', 'X', 'E', 'NWYT', 'X',
           'NW', 'X', 'X', 'X', 'X', 'S', 'X', 'X',
           'W', 'X', 'X', 'X', 'X', 'NEBC', 'W', 'S',
           'W', 'X', 'X', 'X', 'X', 'X', 'E', 'NW'
     ])

QUAD_3B = compile_board(
    ['NW', 'N', 'NS', 'N', 'NE', 'NW', 'N', 'N',
           'W', 'E', 'NWYC', 'X', 'X', 'X', 'X', 'X',
           'W', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
           'W', 'X', 'X', 'X', 'X', 'E', 'SWBT', 'X',
           'SW', 'X', 'X', 'X', 'S', 'X', 'N', 'X',
           'NW', 'X', 'X', 'X', 'NERQ', 'W', 'X', 'X',
           'W', 'SEGH', 'W', 'X', 'X', 'X', 'X', 'S',
           'W', 'N', 'X', 'X', 'X', 'X', 'E', 'NW'
     ])

QUAD_4B = compile_board(
    ['NW', 'N', 'N', 'NE', 'NW', 'N', 'N', 'N',
           'WE', 'SWRT', 'X', 'X', 'X', 'X', 'S', 'X',
           'W', 'N', 'X', 'X', 'X', 'X', 'NEGC', 'W',
           'W', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
           'W', 'X', 'SEBH', 'W', 'X', 'X', 'X', 'S',
           'SW', 'X', 'N', 'X', 'X', 'X', 'E', 'NWYQ',
           'NW', 'X', 'X', 'X', 'X', 'X', 'X', 'S',
           'W', 'X', 'X', 'X', 'X', 'X', 'E', 'NW'
     ])

BOARD_PAIRS = [
    (QUAD_1A, QUAD_1B),
    (QUAD_2A, QUAD_2B),
    (QUAD_3A, QUAD_3B),
    (QUAD_4A, QUAD_4B),
]

BOARDS = [
    QUAD_1A,
    QUAD_1B,
    QUAD_2A,
    QUAD_2B,
    QUAD_3A,
    QUAD_3B,
    QUAD_4A,
    QUAD_4B,
]


def rotate_square_clockwise(sq_vals, num_rotations=1):
    new_sq_vals = sq_vals
    for _ in range(num_rotations):
        sq_vals = new_sq_vals
        new_sq_vals = ''
        for val in sq_vals:
            if val in rotated_wall_transformations:
                new_sq_vals += rotated_wall_transformations[val]
            else:
                new_sq_vals += val
    return new_sq_vals


rotate_squares_clockwise = numpy.vectorize(rotate_square_clockwise)


def rotate_quad_clockwise(quad, num_rotations=1):
    return rotate_squares_clockwise(numpy.rot90(quad, -num_rotations), num_rotations)


def combine_quads_into_single_board(top_left, top_right, bottom_left, bottom_right):
    top_left = rotate_quad_clockwise(top_left, 0)
    top_right = rotate_quad_clockwise(top_right, 1)
    bottom_left = rotate_quad_clockwise(bottom_left, 3)
    bottom_right = rotate_quad_clockwise(bottom_right, 2)

    return numpy.bmat([[top_left, top_right], [bottom_left, bottom_right]])


def printable_board(board, robot_positions):
    """Output the board as a printable string, to help visualize the configuration.

    Eventually, we will want something to output the board as a proper image as well,
    but this is useful for command-line interactive debugging.

    The board will output '#' as walls, '|' and '-' as normal (unobstructed) grid lines.
    If it is a goal tile, it will be identified as such in the upper two characters of the tile.
    If there is a robot on the tile, it will be identified by its color string in the lower-left
    character of the tile.
    """
    out = numpy.full((board.shape[0], board.shape[
                     1], 4, 4), ' ', dtype=numpy.str_)
    for y in range(board.shape[0]):
        for x in range(board.shape[1]):
            chars = ''.join(
                (c for c in board[y, x] if c not in DIRECTIONS + ('X',)))
            if len(chars) > 0:
                out[y, x, 1, 1] = chars[0]
            if len(chars) > 1:
                out[y, x, 1, 2] = chars[1]
            if (y, x) in robot_positions:
                out[y, x, 2, 1] = COLORS[robot_positions.index((y, x))]
            out[y, x, 0, 1:3].fill('#' if 'N' in board[y, x] else '-')
            out[y, x, 1:3, 0].fill('#' if 'W' in board[y, x] else '|')
            out[y, x, 3, 1:3].fill('#' if 'S' in board[y, x] else '-')
            out[y, x, 1:3, 3].fill('#' if 'E' in board[y, x] else '|')

    result = ''
    for y in range(board.shape[0]):
        for i in range(4 if y == board.shape[0] - 1 else 3):
            for x in range(board.shape[1]):
                for j in range(4 if x == board.shape[1] - 1 else 3):
                    result += out[y, x, i, j]
            result += '\n'
    return result
