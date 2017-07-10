#!/usr/bin/python3

import argparse

import BoardConfig
import RicochetRobots
import util


def main():
    parser = argparse.ArgumentParser(
        description='Find an optimal solution for a given board.')
    util.add_board_args(parser)
    parser.add_argument('goal', type=util.parse_tuple,
                        help='Goal square to try to reach')
    args = parser.parse_args()
    board = util.get_full_board(args.boards)
    solver = RicochetRobots.RRobots(board)
    solution = solver.breadth_first_search(args.goal, args.robots)[1:]
    print('{} move{}:'.format(len(solution), '' if len(solution) == 1 else 's'))
    for step in solution[1:]:
        print(', '.join((str(robot) for robot in step)))


if __name__ == '__main__':
    main()
