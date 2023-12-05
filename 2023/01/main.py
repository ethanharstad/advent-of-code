numerals = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

score = 0
with open('input.txt') as f:
    for line in f:
        x = []
        for i, c in enumerate(line):
            if c.isdigit():
                x.append(c)
            for d, numeral in enumerate(numerals):
                if line[i:].startswith(numeral):
                    x.append(str(d+1))
        val = int(x[0] + x[-1])
        score += val

print(score)