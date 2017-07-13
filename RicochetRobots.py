import BoardConfig
import queue
import cProfile
import numpy

import sys


class RRobots:
    direction_offset = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}
    robot_position_color_index = {"R": 0, "Y": 1, "G": 2, "B": 3}

    def __init__(self, board_configuration):
        self.board_configuration = board_configuration

    def breadth_first_search(self, goal_sq_index, starting_robot_positions=((0, 0), (0, 1), (0, 2), (0, 3))):
        """
        :param goal_sq_index: 2-tuple of (row, column) indicating the goal square
        :param starting_robot_positions: tuple of (row, column) pairs, length 4, containing the initial robot positions
            Ex: ((0, 0), (1, 9), (14, 6), (15, 15))
        :return: Path as a list of successive robot positions leading to goal
        """
        seen_robot_positions = set()
        q = queue.Queue()
        q.put([starting_robot_positions])
        goal_robot_position_index = self.get_index_of_goal_robot(goal_sq_index)
        while q:
            current_path = q.get()
            final_position = current_path[-1]
            if final_position[goal_robot_position_index] == goal_sq_index:
                return current_path
            for successor in self.successor_robot_positions(final_position):
                if successor not in seen_robot_positions:
                    seen_robot_positions.add(successor)
                    q.put(current_path + [successor])
        return "No path exists!"

    def get_index_of_goal_robot(self, goal_sq_index):
        try:
            goal_color = set(self.board_configuration[goal_sq_index]) \
                .intersection(set(BoardConfig.COLORS)).pop()
        except KeyError:
            raise KeyError("Invalid goal square")
        return BoardConfig.COLORS.index(goal_color)

    def destination_sq(self, direction, starting_sq, robot_positions_set):
        current_sq = starting_sq

        def tuple_add(a, b):
            return (a[0] + b[0], a[1] + b[1])

        while direction not in self.board_configuration[current_sq]:
            next_sq = tuple_add(current_sq, self.direction_offset[direction])
            if next_sq in robot_positions_set:
                break
            current_sq = next_sq

        return current_sq

    def successor_robot_positions(self, robot_positions):
        successors = []
        robot_positions_set = set(robot_positions)
        for i, robot_position in enumerate(robot_positions):
            for direction in BoardConfig.DIRECTIONS:
                successor_sq = self.destination_sq(
                    direction, robot_position, robot_positions_set)
                successor_positions = list(robot_positions)
                successor_positions[i] = successor_sq
                successors.append(tuple(successor_positions))

        return successors

# cProfile.run("rr.breadth_first_search((13, 1), ((0, 0), (4, 7), (5, 12), (2, 1)))") # 7 moves
# cProfile.run("rr.breadth_first_search((9, 13), ((0, 0), (4, 7), (5, 12),
# (2, 1)))") # 10 moves
