from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=1)
data   = puzzle.input_data.split("\n")

codes_first  = sorted([int(item.split()[0]) for item in data])
codes_second = sorted([int(item.split()[1]) for item in data])

answer_a = sum([abs(a-b) for a, b in zip(codes_first, codes_second)])
answer_b = sum([sum([b for b in codes_second if a == b]) for a in codes_first])

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b