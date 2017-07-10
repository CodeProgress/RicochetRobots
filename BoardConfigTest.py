import unittest
import numpy

import BoardConfig


def rotated(l, amount):
    while amount < 0:
        amount += len(l)
    while amount >= len(l):
        amount -= len(l)
    return l[amount:] + l[:amount]


def numpy_indexer(shape):
    return numpy.array(list(numpy.ndindex(*shape))).reshape(tuple(shape) + (2,))


class BoardConfigTest(unittest.TestCase):

    def check_square_rotation(self, original, new, rotation_amount):
        for c in original:
            if c in BoardConfig.DIRECTIONS:
                i = BoardConfig.DIRECTIONS.index(c)
                self.assertTrue(rotated(BoardConfig.DIRECTIONS,
                                        rotation_amount)[i] in new)
            else:
                self.assertTrue(c in new)

    def test_single_rotate(self):
        for rotation in range(0, 5):
            for original, expected in zip(BoardConfig.DIRECTIONS, rotated(BoardConfig.DIRECTIONS, rotation)):
                self.assertEqual(
                    expected, BoardConfig.rotate_square_clockwise(original, rotation))

    def test_quad_rotate(self):
        for config in BoardConfig.BOARDS:
            for rotation in range(4):
                indexer = numpy.rot90(numpy_indexer(config.shape), -rotation)
                rotated_config = BoardConfig.rotate_quad_clockwise(
                    config, rotation)
                for index in numpy.ndindex(config.shape):
                    self.check_square_rotation(
                        config[tuple(indexer[index])], rotated_config[index], rotation)
