# RicochetRobots

![Reference Board](https://github.com/CodeProgress/RicochetRobots/blob/master/ricochet_robots_reference_board.jpg?raw=true)


# Board Indices:

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

# Robot Positions

Board state is maintained by a tuple, of length four, containing the index of each robot by color:
* (red_index, yellow_index, green_index, blue_index)

For example, the reference board is described as:
* (0, 71, 92, 33)

|      Robot   | Index on board |
| ------------- |-------------|
| Red      | 0 |
| Yellow      | 71 |
| Green      | 92 |
| Blue      | 33 |

# Quadrants

There are eight quadrants.
* QUAD_1A
* QUAD_2A
* QUAD_3A
* QUAD_4A
* QUAD_1B
* QUAD_2B
* QUAD_3B
* QUAD_4B

Each quadrant is a 16x16 section.

Four sections combine to make the board in the following manner:

|      top_left   | top_right|
| ------------- |-------------|
| bottom_left      | bottom_right |


The Reference Board is:

|      QUAD_4A   | QUAD_1B|
| ------------- |-------------|
| QUAD_2B      | QUAD_3A |


# Example solution

```python
board = BoardConfig.combine_quads_into_single_board(
    BoardConfig.QUAD_4A,
    BoardConfig.QUAD_1B,
    BoardConfig.QUAD_2B,
    BoardConfig.QUAD_3A)

rr = RRobots(board)

path = rr.breadth_first_search(37, (0, 71, 92, 33))

print(path)

# [(0, 71, 92, 33), (0, 71, 92, 37)]

```


Explanation:
* The goal square (37) corresponds to the blue hexagon
* Therefore the goal is to move the blue robot to index 37
* The blue robot starts on index 33
* The final path shows the blue robot moving from index 33 to 37


# Requirements:
* Python 3