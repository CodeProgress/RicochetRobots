import BoardConfig
import queue


class RRobots:
    def __init__(self, board_configuration):
        self.board_configuration = board_configuration
        self.direction_offset = {"N": -16, "E": 1, "S": 16, "W": -1}
        self.robot_position_color_index = {"R": 0, "Y": 1, "G": 2, "B": 3}

    def breadth_first_search(self, goal_sq_index, starting_robot_positions=(0, 1, 2, 3)):
        """
        :param goal_sq_index: 0 <= int 0 <= 255
        :param starting_robot_positions: tuple of ints between 0 and 255 inclusive, length 4
            Ex: (0, 23, 230, 255)
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
        return self.robot_position_color_index[goal_color]

    @staticmethod
    def is_sq_on_board(sq):
        return 0 <= sq <= 255

    def destination_sq(self, direction, starting_sq, robot_positions):
        current_sq = starting_sq

        while direction not in self.board_configuration[current_sq]:
            next_sq = current_sq + self.direction_offset[direction]
            if not self.is_sq_on_board(next_sq):
                break
            if next_sq in robot_positions:
                break
            current_sq = next_sq

        return current_sq

    def successor_robot_positions(self, robot_positions):
        successors = []

        for i, robot_position in enumerate(robot_positions):
            for direction in "NESW":
                successor_sq = self.destination_sq(direction, robot_position, robot_positions)
                successor_positions = list(robot_positions)
                successor_positions[i] = successor_sq
                successors.append(tuple(successor_positions))

        return successors

board = BoardConfig.combine_quads_into_single_board(
    BoardConfig.QUAD_4A,
    BoardConfig.QUAD_1B,
    BoardConfig.QUAD_2B,
    BoardConfig.QUAD_3A)

rr = RRobots(board)

# BoardConfig.QUAD_4A, BoardConfig.QUAD_1B, BoardConfig.QUAD_2B, BoardConfig.QUAD_3A
assert rr.breadth_first_search(37, (0, 71, 92, 33)) \
       == [(0, 71, 92, 33),
           (0, 71, 92, 37)]

# BoardConfig.QUAD_4A, BoardConfig.QUAD_1B, BoardConfig.QUAD_2B, BoardConfig.QUAD_3A
assert rr.breadth_first_search(37, (4, 71, 92, 7)) \
       == [(4, 71, 92, 7),
           (4, 71, 92, 5),
           (4, 71, 92, 37)]

# BoardConfig.QUAD_4A, BoardConfig.QUAD_1B, BoardConfig.QUAD_2B, BoardConfig.QUAD_3A
assert rr.breadth_first_search(37, (116, 71, 92, 104)) \
       == [(116, 71, 92, 104),
           (4, 71, 92, 104),
           (4, 71, 92, 8),
           (4, 71, 92, 5),
           (4, 71, 92, 37)]

# BoardConfig.QUAD_4A, BoardConfig.QUAD_1B, BoardConfig.QUAD_2B, BoardConfig.QUAD_3A
assert rr.breadth_first_search(37, (0, 71, 92, 6)) \
       == [(0, 71, 92, 6),
           (0, 71, 92, 9),
           (0, 7, 92, 9),
           (0, 4, 92, 9),
           (0, 4, 92, 5),
           (0, 4, 92, 37)]

path = rr.breadth_first_search(37, (0, 71, 92, 33))

print(path)
