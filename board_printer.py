#!/usr/bin/python3

import argparse

import BoardConfig
import util


def main():
    parser = argparse.ArgumentParser(
        description='Print a given board configuration out to the console')
    util.add_board_args(parser)
    args = parser.parse_args()
    board = util.get_full_board(args.boards)
    print(BoardConfig.printable_board(board, args.robots))


if __name__ == '__main__':
    main()
