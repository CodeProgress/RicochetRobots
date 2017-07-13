import unittest

from collections import namedtuple

import RicochetRobots
import BoardConfig

Configuration = namedtuple(
    'Configuration', ('goal', 'positions', 'optimal', 'expected'))
Configuration.__new__.__defaults__ = (None)


class TestRobotSolver(unittest.TestCase):

    def setUp(self):
        self.board = BoardConfig.combine_quads_into_single_board(
            BoardConfig.QUAD_4A,
            BoardConfig.QUAD_1B,
            BoardConfig.QUAD_2B,
            BoardConfig.QUAD_3A)
        self.solver = RicochetRobots.RRobots(self.board)

    def stringify_list(self, solution):
        return '\n'.join([str(s) for s in solution])

    def test_basic_solve(self):
        configurations = [
            Configuration((2, 5), ((0, 0), (4, 7), (5, 12), (2, 1)), 2,
                          [
                ((0, 0), (4, 7), (5, 12), (2, 1)),
                ((0, 0), (4, 7), (5, 12), (2, 5)),
            ]),
            Configuration((2, 5), ((0, 4), (4, 7), (5, 12), (0, 7)), 3,
                          [
                ((0, 4), (4, 7), (5, 12), (0, 7)),
                ((0, 4), (4, 7), (5, 12), (0, 5)),
                ((0, 4), (4, 7), (5, 12), (2, 5)),
            ]),
            Configuration((2, 5), ((7, 4), (4, 7), (5, 12), (6, 8)), 5,
                          [
                ((7, 4), (4, 7), (5, 12), (6, 8)),
                ((0, 4), (4, 7), (5, 12), (6, 8)),
                ((0, 4), (4, 7), (5, 12), (0, 8)),
                ((0, 4), (4, 7), (5, 12), (0, 5)),
                ((0, 4), (4, 7), (5, 12), (2, 5)),
            ]),
            Configuration((2, 5), ((0, 0), (4, 7), (5, 12), (0, 6)), 6,
                          [
                ((0, 0), (4, 7), (5, 12), (0, 6)),
                ((0, 0), (4, 7), (5, 12), (0, 9)),
                ((0, 0), (0, 7), (5, 12), (0, 9)),
                ((0, 0), (0, 4), (5, 12), (0, 9)),
                ((0, 0), (0, 4), (5, 12), (0, 5)),
                ((0, 0), (0, 4), (5, 12), (2, 5)),
            ]),
        ]

        for configuration in configurations:
            solution = self.solver.breadth_first_search(
                configuration.goal, configuration.positions)
            self.assertEqual(solution[0], configuration.positions, 'Solution {} does not have original configuration {}'.format(
                self.stringify_list(solution), configuration.positions))
            self.assertTrue(configuration.goal in solution[-1], 'Solution {} does not reach goal {}'.format(
                self.stringify_list(solution), configuration.goal))
            self.assertEqual(configuration.optimal, len(
                solution), 'Solution {} has incorrect length'.format(self.stringify_list(solution)))
            if configuration.expected is not None:
                self.assertEqual(configuration.expected, solution)
