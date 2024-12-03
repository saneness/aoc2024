from aocd.models import Puzzle
import re

puzzle = Puzzle(year=2024, day=3)
data   = puzzle.input_data

rx = re.compile("mul\((\d+),(\d+)\)|(don't\(\)|do\(\))", re.VERBOSE)

answer_a = 0
answer_b = 0

do = True
for item in re.findall(rx, data):
    if item[2] == "":
        answer_a += int(item[0])*int(item[1])
        answer_b += int(item[0])*int(item[1]) if do else 0
    else:
        do = item[2] == "do()"

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b