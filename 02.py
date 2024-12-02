from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=2)
data   = [[int(subitem) for subitem in item.split()] for item in puzzle.input_data.split("\n")]

def check(item):
    if (sorted(item)==item or sorted(item)[::-1]==item) and sorted(list(set(item)))==sorted(item) and max([abs(next-current) for current, next in zip(item[:-1], item[1:])]) <= 3:
        return 1
    else:
        return 0

answer_a = 0
answer_b = 0

for item in data:
    if check(item):
        answer_a += 1
        answer_b += 1
    else:
        answer_b += int(sum([check(item[:i]+item[i+1:]) for i, _ in enumerate(item)]) > 0)

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b