#!/bin/python3

from collections import Counter

def day_01():
    print("########## Day 01 ##########")

    lines = []

    with open("input/input_01.txt", "r") as file:
        lines = file.readlines()

    elfs_calories = []
    total = 0

    for line in lines:
        if line != '\n':
            total += int(line)
        else:
            elfs_calories.append(total)
            total = 0

    elfs_calories.sort(reverse=True)

    print(f"Part 1 : {elfs_calories[0]}")
    print(f"Part 2 : {elfs_calories[0] + elfs_calories[1] + elfs_calories[2]}")

def day_02():
    print("########## Day 02 ##########")

    lines = []

    with open("input/input_02.txt", "r") as file:
        lines = file.readlines()

    ROCK = 'ROCK'
    PAPER = 'PAPER'
    SCISSORS = 'SCISSORS'

    LOSE = 'LOSE'
    DRAW = 'DRAW'
    WIN = 'WIN'

    part1_values = {
        'A': ROCK,
        'B': PAPER,
        'C': SCISSORS,
        'X': ROCK,
        'Y': PAPER,
        'Z': SCISSORS
    }

    part2_values = {
        'A': ROCK,
        'B': PAPER,
        'C': SCISSORS,
        'X': LOSE,
        'Y': DRAW,
        'Z': WIN
    }

    part2_plays = {
        LOSE: {
            ROCK: SCISSORS,
            PAPER: ROCK,
            SCISSORS: PAPER
        },
        DRAW: {
            ROCK: ROCK,
            PAPER: PAPER,
            SCISSORS: SCISSORS
        },
        WIN : {
            ROCK: PAPER,
            PAPER: SCISSORS,
            SCISSORS: ROCK
        }
    }

    play_values = {
        ROCK: 1,
        PAPER: 2,
        SCISSORS: 3
    }

    total_score_part1 = 0
    total_score_part2 = 0

    for line in lines:
        # Part 1
        opponent_play = part1_values.get(line.split()[0])
        my_play = part1_values.get(line.split()[1])

        round_score = 0
        round_score = play_values.get(my_play)

        # DRAW
        if opponent_play == my_play:
            round_score += 3
        # WIN
        elif (opponent_play == ROCK and my_play == PAPER) or (opponent_play == PAPER and my_play == SCISSORS) or (opponent_play == SCISSORS and my_play == ROCK):
            round_score += 6
        # LOSE
        else:
            round_score += 0

        total_score_part1 += round_score

        # Part 2
        opponent_play = part2_values.get(line.split()[0])
        round_end = part2_values.get(line.split()[1])

        my_play = part2_plays.get(round_end).get(opponent_play)

        round_score = 0
        round_score = play_values.get(my_play)

        # DRAW
        if opponent_play == my_play:
            round_score += 3
        # WIN
        elif (opponent_play == ROCK and my_play == PAPER) or (opponent_play == PAPER and my_play == SCISSORS) or (opponent_play == SCISSORS and my_play == ROCK):
            round_score += 6
        # LOSE
        else:
            round_score += 0

        total_score_part2 += round_score

    print(f"Part 1 : {total_score_part1}")
    print(f"Part 2 : {total_score_part2}")

def day_03():
    print("########## Day 03 ##########")

    lines = []

    with open("input/input_03.txt", "r") as file:
        lines = file.readlines()

    alphabet_min = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_maj = alphabet_min.upper()
    alphabet = alphabet_min + alphabet_maj

    total_priority_part1 = 0
    total_priority_part2 = 0

    groups = []
    group = []

    for index, line in enumerate(lines):
        cleared_line = line.replace('\n', '')

        # Part 1
        half_line = int(len(cleared_line) / 2)
        first_compartiment = Counter(cleared_line[:half_line])
        second_compartiment = Counter(cleared_line[half_line:])

        unique_item = None

        for first_key, first_value in first_compartiment.items():
            for second_key, second_value in second_compartiment.items():
                if first_key == second_key:
                    unique_item = first_key
        
        if unique_item:
            total_priority_part1 += alphabet.index(unique_item) + 1

        # Part 2
        if index % 3 == 0 and index != 0:
            groups.append(group)
            group = [cleared_line]
        else:
            group.append(cleared_line)

    # Append last group
    groups.append(group)

    for group in groups:
        item = ""
        counters = [list(Counter(rucksack).keys()) for rucksack in group]

        inter = set(counters[0])
        inter.intersection_update(counters[1])
        inter.intersection_update(counters[2])

        for value in inter:
            item += value

        total_priority_part2 += alphabet.index(item) + 1

    print(f"Part 1 : {total_priority_part1}")
    print(f"Part 2 : {total_priority_part2}")

def day_04():
    print("########## Day 04 ##########")

    lines = []

    with open("input/input_04.txt", "r") as file:
        lines = file.readlines()

    nb_superposition = 0
    nb_overlap = 0

    for line in lines:
        pairs = line.replace('\n', '').split(',')

        elf_1 = {
            'start': int(pairs[0].split('-')[0]),
            'end': int(pairs[0].split('-')[1]),
        }
        elf_2 = {
            'start': int(pairs[1].split('-')[0]),
            'end': int(pairs[1].split('-')[1]),
        }

        # Elf 1 section inside elf 2 section
        if elf_1.get('start') >= elf_2.get('start') and elf_1.get('end') <= elf_2.get('end'):
            nb_superposition += 1
        
        # Elf 2 section inside elf 1 section
        elif elf_2.get('start') >= elf_1.get('start') and elf_2.get('end') <= elf_1.get('end'):
            nb_superposition += 1

        # Elf 1 start or end in elf 2 section
        elif (elf_2.get('end') >= elf_1.get('start') >= elf_2.get('start')) or (elf_2.get('end') >= elf_1.get('end') >= elf_2.get('start')):
            nb_overlap += 1
    
    nb_overlap += nb_superposition

    print(f"Part 1 : {nb_superposition}")
    print(f"Part 2 : {nb_overlap}")

if __name__ == '__main__':
    day_01()
    day_02()
    day_03()
    day_04()