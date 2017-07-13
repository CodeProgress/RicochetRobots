import argparse

import BoardConfig


def board_choices():
    for i in range(1, 5):
        for c in ('A', 'B'):
            yield str(i) + c


def parse_tuple(x):
    result = tuple([int(c) for c in x.split(',')])
    if len(result) != 2:
        raise Exception('Invalid co-ordinate {}'.format(x))
    return result


def add_board_args(parser):
    parser.add_argument('boards', nargs=4, choices=tuple(board_choices()), type=str.upper,
                        help='Board pieces to use, in clockwise order, starting from the top-left')
    parser.add_argument('robots', nargs=4, type=parse_tuple,
                        help='Locations of the four robots, in the order Red, Yellow, Green, Blue')
    return parser


def get_board_quad(board):
    index = ord(board[0]) - ord('1')
    ab = ord(board[1]) - ord('A')
    return BoardConfig.BOARD_PAIRS[index][ab]


def get_full_board(boards):
    return BoardConfig.combine_quads_into_single_board(*[get_board_quad(x) for x in boards])
