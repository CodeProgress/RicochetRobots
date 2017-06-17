
# Directions
NORTH = 'N'
EAST = 'E'
SOUTH = 'S'
WEST = 'W'

# Colors
RED = 'R'
YELLOW = 'Y'
GREEN = 'G'
BLUE = 'B'

COLORS = [RED, YELLOW, GREEN, BLUE]

# Shapes
CIRCLE = 'C'
TRIANGLE = 'T'
SQUARE = 'Q'
HEXAGON = 'H'

rotated_wall_transformations = {
    NORTH: EAST,
    EAST: SOUTH,
    SOUTH: WEST,
    WEST: NORTH,
}

# Boards adapted from https://github.com/fogleman/Ricochet/blob/master/model.py

# Quads
QUAD_1A = ['NW', 'N', 'N', 'N', 'NE', 'NW', 'N', 'N',
           'W', 'S', 'X', 'X', 'X', 'X', 'SEYH', 'W',
           'WE', 'NWGT', 'X', 'X', 'X', 'X', 'N', 'X',
           'W', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
           'W',  'X', 'X', 'X', 'X', 'X', 'S', 'X',
           'SW', 'X', 'X', 'X', 'X', 'X', 'NEBQ', 'W',
           'NW', 'X', 'E', 'SWRC', 'X', 'X', 'X', 'S',
           'W', 'X',  'X', 'N', 'X', 'X', 'E', 'NW'
           ]

QUAD_2A = ['NW', 'N', 'N', 'NE', 'NW', 'N', 'N', 'N',
           'W', 'X', 'X', 'X', 'X', 'E', 'SWBC', 'X',
           'W', 'S', 'X', 'X', 'X', 'X', 'N', 'X',
           'W', 'NEYT', 'W', 'X', 'X', 'S', 'X', 'X',
           'W', 'X', 'X', 'X', 'E', 'NWGQ', 'X', 'X',
           'W', 'X', 'SERH', 'W', 'X', 'X', 'X', 'X',
           'SW', 'X', 'N', 'X', 'X', 'X', 'X', 'S',
           'NW', 'X', 'X', 'X', 'X', 'X', 'E', 'NW'
           ]

QUAD_3A = ['NW', 'N', 'N', 'NE', 'NW', 'N', 'N', 'N',
           'W', 'X', 'X', 'X', 'X', 'SEGH', 'W', 'X',
           'WE', 'SWRQ', 'X', 'X', 'X', 'N', 'X', 'X',
           'SW', 'N', 'X', 'X', 'X', 'X', 'S', 'X',
           'NW', 'X', 'X', 'X', 'X', 'E', 'NWYC', 'X',
           'W', 'X', 'S', 'X', 'X', 'X', 'X', 'X',
           'W', 'X', 'NEBT', 'W', 'X', 'X', 'X', 'S',
           'W', 'X', 'X', 'X', 'X', 'X', 'E', 'NW'
           ]

QUAD_4A = ['NW', 'N', 'N', 'NE', 'NW', 'N', 'N', 'N',
           'W', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
           'W', 'X', 'X', 'X', 'X', 'SEBH', 'W', 'X',
           'W', 'X', 'S', 'X', 'X', 'N', 'X', 'X',
           'SW', 'X', 'NEGC', 'W', 'X', 'X', 'X', 'X',
           'NW', 'S', 'X', 'X', 'X', 'X', 'E', 'SWRT',
           'WE', 'NWYQ', 'X', 'X', 'X', 'X', 'X', 'NS',
           'W', 'X', 'X', 'X', 'X', 'X', 'E', 'NW'
           ]

QUAD_1B = ['NW', 'NE', 'NW', 'N', 'NS', 'N', 'N', 'N',
           'W', 'S', 'X', 'E', 'NWRC', 'X', 'X', 'X',
           'W', 'NEGT', 'W', 'X', 'X', 'X', 'X', 'X',
           'W', 'X', 'X', 'X', 'X', 'X', 'SEYH', 'W',
           'W', 'X', 'X', 'X', 'X', 'X', 'N', 'X',
           'SW', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
           'NW', 'X', 'E', 'SWBQ', 'X', 'X', 'X', 'S',
           'W', 'X', 'X', 'N', 'X', 'X', 'E', 'NW'
           ]

QUAD_2B = ['NW', 'N', 'N', 'N', 'NE', 'NW', 'N', 'N',
           'W', 'X', 'SERH', 'W', 'X', 'X', 'X', 'X',
           'W', 'X', 'N', 'X', 'X', 'X', 'X', 'X',
           'WE', 'SWGQ', 'X', 'X', 'X', 'X', 'S', 'X',
           'SW', 'N', 'X', 'X', 'X', 'E', 'NWYT', 'X',
           'NW', 'X', 'X', 'X', 'X', 'S', 'X', 'X',
           'W', 'X', 'X', 'X', 'X', 'NEBC', 'W', 'S',
           'W', 'X', 'X', 'X', 'X', 'X', 'E', 'NW'
           ]

QUAD_3B = ['NW', 'N', 'NS', 'N', 'NE', 'NW', 'N', 'N',
           'W', 'E', 'NWYC', 'X', 'X', 'X', 'X', 'X',
           'W', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
           'W', 'X', 'X', 'X', 'X', 'E', 'SWBT', 'X',
           'SW', 'X', 'X', 'X', 'S', 'X', 'N', 'X',
           'NW', 'X', 'X', 'X', 'NERQ', 'W', 'X', 'X',
           'W', 'SEGH', 'W', 'X', 'X', 'X', 'X', 'S',
           'W', 'N', 'X', 'X', 'X', 'X', 'E', 'NW'
           ]

QUAD_4B = ['NW', 'N', 'N', 'NE', 'NW', 'N', 'N', 'N',
           'WE', 'SWRT', 'X', 'X', 'X', 'X', 'S', 'X',
           'W', 'N', 'X', 'X', 'X', 'X', 'NEGC', 'W',
           'W', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
           'W', 'X', 'SEBH', 'W', 'X', 'X', 'X', 'S',
           'SW', 'X', 'N', 'X', 'X', 'X', 'E', 'NWYQ',
           'NW', 'X', 'X', 'X', 'X', 'X', 'X', 'S',
           'W', 'X', 'X', 'X', 'X', 'X', 'E', 'NW'
           ]


top_left_indices = [
    0,   1,   2,   3,   4,   5,   6,   7,
    16,  17,  18,  19,  20,  21,  22,  23,
    32,  33,  34,  35,  36,  37,  38,  39,
    48,  49,  50,  51,  52,  53,  54,  55,
    64,  65,  66,  67,  68,  69,  70,  71,
    80,  81,  82,  83,  84,  85,  86,  87,
    96,  97,  98,  99,  100, 101, 102, 103,
    112, 113, 114, 115, 116, 117, 118, 119
    ]

top_right_indices = [
    8,   9,   10,  11,  12,  13,  14,  15,
    24,  25,  26,  27,  28,  29,  30,  31,
    40,  41,  42,  43,  44,  45,  46,  47,
    56,  57,  58,  59,  60,  61,  62,  63,
    72,  73,  74,  75,  76,  77,  78,  79,
    88,  89,  90,  91,  92,  93,  94,  95,
    104, 105, 106, 107, 108, 109, 110, 111,
    120, 121, 122, 123, 124, 125, 126, 127
    ]

bottom_left_indices = [
    128, 129, 130, 131, 132, 133, 134, 135,
    144, 145, 146, 147, 148, 149, 150, 151,
    160, 161, 162, 163, 164, 165, 166, 167,
    176, 177, 178, 179, 180, 181, 182, 183,
    192, 193, 194, 195, 196, 197, 198, 199,
    208, 209, 210, 211, 212, 213, 214, 215,
    224, 225, 226, 227, 228, 229, 230, 231,
    240, 241, 242, 243, 244, 245, 246, 247
    ]

bottom_right_indices = [
    136, 137, 138, 139, 140, 141, 142, 143,
    152, 153, 154, 155, 156, 157, 158, 159,
    168, 169, 170, 171, 172, 173, 174, 175,
    184, 185, 186, 187, 188, 189, 190, 191,
    200, 201, 202, 203, 204, 205, 206, 207,
    216, 217, 218, 219, 220, 221, 222, 223,
    232, 233, 234, 235, 236, 237, 238, 239,
    248, 249, 250, 251, 252, 253, 254, 255
    ]

clockwise_rotated_indices = [
    56, 48, 40, 32, 24, 16, 8, 0,
    57, 49, 41, 33, 25, 17, 9, 1,
    58, 50, 42, 34, 26, 18, 10, 2,
    59, 51, 43, 35, 27, 19, 11, 3,
    60, 52, 44, 36, 28, 20, 12, 4,
    61, 53, 45, 37, 29, 21, 13, 5,
    62, 54, 46, 38, 30, 22, 14, 6,
    63, 55, 47, 39, 31, 23, 15, 7
]


"""
Combined board indices:
    0   1   2   3   4   5   6   7    8   9   10  11  12  13  14  15
    16  17  18  19  20  21  22  23   24  25  26  27  28  29  30  31
    32  33  34  35  36  37  38  39   40  41  42  43  44  45  46  47
    48  49  50  51  52  53  54  55   56  57  58  59  60  61  62  63
    64  65  66  67  68  69  70  71   72  73  74  75  76  77  78  79
    80  81  82  83  84  85  86  87   88  89  90  91  92  93  94  95
    96  97  98  99  100 101 102 103  104 105 106 107 108 109 110 111
    112 113 114 115 116 117 118 119  120 121 122 123 124 125 126 127

    128 129 130 131 132 133 134 135  136 137 138 139 140 141 142 143
    144 145 146 147 148 149 150 151  152 153 154 155 156 157 158 159
    160 161 162 163 164 165 166 167  168 169 170 171 172 173 174 175
    176 177 178 179 180 181 182 183  184 185 186 187 188 189 190 191
    192 193 194 195 196 197 198 199  200 201 202 203 204 205 206 207
    208 209 210 211 212 213 214 215  216 217 218 219 220 221 222 223
    224 225 226 227 228 229 230 231  232 233 234 235 236 237 238 239
    240 241 242 243 244 245 246 247  248 249 250 251 252 253 254 255
"""


def get_new_array_after_remapping(old_array, index_remapping):
    """Mutates the new_array parameter"""
    new_array = [0] * len(old_array)
    for i in range(len(old_array)):
        index_of_updated_value = index_remapping[i]
        new_array[i] = old_array[index_of_updated_value]
    return new_array


def rotate_walls_clockwise(quad):
    for i, sq_vals in enumerate(quad):
        new_sq_vals = ""
        for val in sq_vals:
            if val in rotated_wall_transformations:
                new_sq_vals += rotated_wall_transformations[val]
            else:
                new_sq_vals += val
        quad[i] = new_sq_vals


def rotate_quad_clockwise(quad, num_rotations=1):
    rotated_quad = quad
    for _ in range(num_rotations):
        rotated_quad = get_new_array_after_remapping(quad, clockwise_rotated_indices)
        rotate_walls_clockwise(rotated_quad)
        quad = rotated_quad
    return rotated_quad


def map_quad_values_onto_board(quad, board, index_mappings):
    for i, val in enumerate(quad):
        board_index = index_mappings[i]
        board[board_index] = val


def combine_quads_into_single_board(top_left, top_right, bottom_left, bottom_right):
    board = [None]*256

    top_left = rotate_quad_clockwise(top_left, 0)
    top_right = rotate_quad_clockwise(top_right, 1)
    bottom_left = rotate_quad_clockwise(bottom_left, 3)
    bottom_right = rotate_quad_clockwise(bottom_right, 2)

    map_quad_values_onto_board(top_left, board, top_left_indices)
    map_quad_values_onto_board(top_right, board, top_right_indices)
    map_quad_values_onto_board(bottom_left, board, bottom_left_indices)
    map_quad_values_onto_board(bottom_right, board, bottom_right_indices)

    return board
