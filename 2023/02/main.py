games = {}

with open('input.txt') as f:
    for line in f:
        id_token, turns = line.split(':')
        id = id_token.split(' ')[-1]
        games[id] = {'red': 0, 'green': 0, 'blue': 0}
        for turn in turns.split(';'):
            for hand in turn.split(','):
                count, color = hand.strip().split(' ')
                games[id][color] = max(int(count), games[id][color])

question = {
    'red': 12,
    'green': 13,
    'blue': 14
}
valid_ids = []
for id, value in games.items():
    for color, count in question.items():
        valid = True
        if value[color] > count:
            valid = False
            break
    if valid:
        valid_ids.append(id)

score = 0
for id in valid_ids:
    score += int(id)

print(f"Sum of valid IDs: {score}")

total_power = 0
for value in games.values():
    power = value['red'] * value['green'] * value['blue']
    total_power += power

print(f"Total Power: {total_power}")