import sys

def parse_nums(s):
    answer = []
    for x in s.strip().split(' '):
        if not x:
            continue
        answer.append(int(x.strip()))
    return answer

def get_matches(winning, values):
    count = 0
    for num in values:
        if num in winning:
            count += 1
    return count

def get_score(matches):
    return 2**(matches-1) if matches > 0 else 0

def copy_cards(cards, index):
    # print(f"Process {index+1}: {cards[index]}")
    count = 1
    matches = cards[index]
    for i in range(matches):
        # print(f"iter {i}: {index+i+1}")
        if index+i+1 > len(cards):
            break
        count += copy_cards(cards, index+i+1)
    print(f"Finished {index+1}: return {count}")
    return count


def run(filename):
    card_matches = []
    total_score = 0
    with open(filename) as f:
        for card in f:
            card_token, numbers = card.split(':')
            a, b = numbers.split('|')
            winning_numbers = parse_nums(a)
            my_numbers = parse_nums(b)
            matches = get_matches(winning_numbers, my_numbers)
            card_matches.append(matches)
            total_score += get_score(matches)
    print(f"Total Score: {total_score}")

    count = 0
    for i in range(len(card_matches)):
        count += copy_cards(card_matches, i)
    print(f"Total Cards: {count}")

if __name__ == "__main__":
    filename = sys.argv[1]
    run(filename)