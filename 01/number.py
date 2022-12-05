with open('tests/input.txt') as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]

elves = []
while len(lines) > 0:
    for i, l in enumerate(lines):
        if l == '':
            break
    elves.append(lines[:i])
    lines = lines[i+1:]
elves = [sum([int(s) for s in e]) for e in elves]
print(sum(sorted(elves)[-3:]))