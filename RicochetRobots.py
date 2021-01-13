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
                    # check on expansion if goal reached. count 23,000 -> 8,000
                    if successor[goal_robot_position_index] == goal_sq_index:
                        return current_path+[successor]
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

    def breadth_first_search_w_priority_queue(self, goal_sq_index, starting_robot_positions):
        """
        experimental update to breadth_first_search function above
            Note: Manually tuned for only the params:  (13, 1), ((0, 0), (4, 7), (5, 12), (2, 1))
        number of nodes explored reduced from 23,000 to 1,642
        TODO: prove heuristic is admissible ( https://en.wikipedia.org/wiki/Admissible_heuristic )
        TODO: explore why two_away_squares is the most effective, while others only make marginal difference
        """
        seen_robot_positions = set()
        q = queue.PriorityQueue()
        q.put((1, [starting_robot_positions]))
        goal_robot_position_index = self.get_index_of_goal_robot(goal_sq_index)
        count = 0
        three_away_squares = {(11, 1), (11, 2), (11, 3), (11, 4), (11, 5),
                              (11, 6), (11, 7), (11, 8), (11, 9),
                              (12, 1), (12, 2), (12, 3), (12, 4), (12, 5),
                              (12, 6), (12, 7),
                              (0, 3), (1, 3), (2, 3),
                              (3, 3), (4, 3), (5, 3), (6, 3), (7, 3),
                              (8, 3), (9, 3), (10, 3), (11, 3), (12, 3), (13, 3),
                              (4, 2), (5, 2), (6, 2), (7, 2),
                              (8, 2), (9, 2), (10, 2), (11, 2), (12, 2), (13, 2),
                              (10, 4), (11, 4), (12, 4), (13,4), (14, 4)
                              }
        two_away_squares = {(11, 0), (12, 0), (14, 0), (15, 0), (14, 2), (14, 3), (15, 2), (15, 3), (15, 4)}
        one_away_squares = {(13, 0), (14, 1), (15, 1)}
        while q:
            count += 1
            current_path = q.get()[1]
            final_position = current_path[-1]
            if final_position[goal_robot_position_index] == goal_sq_index:
                return current_path, count
            for successor in self.successor_robot_positions(final_position):
                if successor not in seen_robot_positions:
                    # check on expansion if goal reached, 1,600 --> 540
                    if successor[goal_robot_position_index] == goal_sq_index:
                        return current_path +[successor], count
                    seen_robot_positions.add(successor)
                    priority = len(current_path)
                    # if set([x for x in successor if x != successor[goal_robot_position_index]]).intersection(three_away_squares):
                    #     priority -= 1 #int(priority)**.5
                    if set([x for x in successor if x != successor[goal_robot_position_index]]).intersection(two_away_squares):
                        priority -= 7 #int(priority)**.5
                    # if set(successor[goal_robot_position_index]).intersection(three_away_squares):
                    #     priority -= 3 #int(priority)**.7
                    # if set(successor[goal_robot_position_index]).intersection(two_away_squares):
                    #     priority -= 4 #int(priority)**.7
                    # elif set(successor[goal_robot_position_index]).intersection(one_away_squares):
                    #     priority -= 5 #priority
                    q.put((priority, current_path + [successor]))
        return "No path exists!"

    def successor_robot_positions_fast(self, robot_positions):
        """Byte arrays?
        Precompute landing squares for NESW for all 256 squares, then quickly update based on robot positions?"""
        pass

    def pre_compute_a_star_heuristic(self, goal_square):
        pass


board = BoardConfig.combine_quads_into_single_board(
    BoardConfig.QUAD_4A,
    BoardConfig.QUAD_1B,
    BoardConfig.QUAD_2B,
    BoardConfig.QUAD_3A)

rr = RRobots(board)

solution = rr.breadth_first_search_w_priority_queue((13, 1), ((0, 0), (4, 7), (5, 12), (2, 1))) # 7 moves
print(solution[1])
for i in solution[0]:
    print(i)

# solution = rr.breadth_first_search_w_priority_queue((13, 1), ((0, 0), (4, 7), (5, 12), (2, 1))) # 7 moves
# print(solution[1])
# for i in solution[0]:
#     print(BoardConfig.printable_board(board, i))

# solution = rr.breadth_first_search((13, 1), ((0, 0), (4, 7), (5, 12), (2, 1))) # 7 moves
# for i in solution:
#     print(i)

# solution2 = rr.breadth_first_search((9, 13), ((0, 0), (4, 7), (5, 12), (2, 1))) # 10 moves
# print(solution2[1])
# for j in solution2[0]:
#     print(j)
