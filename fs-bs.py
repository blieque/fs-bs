#!/usr/bin/env python3

import shutil
import random

# characters the script can pick from
CHARS = [
  '\ue000',
  '\ue001',
  '\ue002',
  '\ue003',
  '\ue004',
  '\ue005',
  '\ue006',
  '\ue007',
  '\ue008',
  '\ue009',
  '\ue00a',
  '\ue00b',
  '\ue00c'
]
# preset colors the script can from, if it isn't randomly generating them
COLORS = [
  [ 80, 216, 216 ],
  [ 216, 80, 216 ],
  [ 216, 216, 80 ]
]

CHAR_MIN = 2
COLOR_MIN = 2

# SET UP RUNTIME ARRAYS

chars = CHARS
colors = COLORS

# remove some of the characters
char_count = len(CHARS)
chars_to_remove = random.randint(1, char_count - CHAR_MIN + 1)
for i in range(1, chars_to_remove):
  del(chars[random.randint(0, char_count - i)])
# inject some spaces
for i in range(0, random.randint(0, round(char_count / 2))):
  chars.append(' ')

# remove some of the colors
color_count = len(COLORS)
colors_to_remove = random.randint(1, color_count - COLOR_MIN + 1)
for i in range(1, colors_to_remove):
  del(colors[random.randint(0, color_count - i)])

char_max = len(chars)
color_max = len(colors)

# GET ROW AND COLUMN COUNTS

columns, rows = shutil.get_terminal_size((10, 10))
rows = 8 # temporary limit for testing

# CREATE OUTPUT VAR WITH BACKGROUND COLOR

background_color = [
  random.randint(0, 64),
  random.randint(0, 64),
  random.randint(0, 64)
]
# output string that will be appended to during the loop
output = "\x1b[48;2;{0};{1};{2}m" \
  .format(background_color[0], background_color[1], background_color[2])

# LOOOOP

for i in range(0, rows):
  for j in range(0, columns):
    char = chars[random.randint(0, char_max - 1)]
    color = colors[random.randint(0, color_max - 1)]

    output += "\x1b[38;2;{0};{1};{2}m{3}" \
      .format(color[0], color[1], color[2], char)
  output

output += "\x1b[0m"

# PARTAY TIME

print(output)
